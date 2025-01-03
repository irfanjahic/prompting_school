<script>
    import { navigate } from 'svelte-routing';
    let email = '';
    let password = '';

    async function handleLogin() {
        try {
            const response = await fetch('http://localhost:5000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email,
                    password
                })
            });
            const data = await response.json();
            if (response.ok) {
                console.log('User logged in successfully:', data);
                // Store the token in localStorage
                localStorage.setItem('authToken', data.token);
                // Navigate to the course page after successful login
                navigate('/course');
            } else {
                console.error('Error logging in:', data.error);
            }
        } catch (error) {
            console.error('Error logging in:', error);
        }
    }
</script>


<style>
    .form-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f9f9f9;
    }

    .form-group {
        display: flex;
        justify-content: space-between;
        margin-bottom: 15px;
    }

    .form-group label {
        flex: 1;
        margin-right: 10px;
        display: flex;
        align-items: center;
    }

    .form-group input {
        flex: 2;
        padding: 8px;
        box-sizing: border-box;
    }

    .form-group button {
        background-color: #007BFF;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    .form-group button:hover {
        background-color: #0056b3;
    }
</style>

<div class="form-container">
    <h2>Log In</h2>
    <form on:submit|preventDefault={handleLogin}>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" bind:value={email} required />
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" bind:value={password} required />
        </div>
        <div class="form-group">
            <button type="submit">Log In</button>
        </div>
    </form>
</div>