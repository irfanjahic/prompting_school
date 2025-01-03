<script>
    import { navigate } from 'svelte-routing';
    let firstName = '';
    let lastName = '';
    let dateOfBirth = '';
    let email = '';
    let password = '';

    async function handleSubmit() {
        try {
            //const response = await fetch('http://localhost:5000/register', {
            const response = await fetch('https://api.irfanjahic.com/register', {    
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    firstName,
                    lastName,
                    dateOfBirth,
                    email,
                    password
                })
            });
            const data = await response.json();
            if (response.ok) {
                console.log('User registered successfully:', data);
                // Navigate to the login page after successful registration
                navigate('/login');
            } else {
                console.error('Error registering user:', data.error);
            }
        } catch (error) {
            console.error('Error registering user:', error);
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
        display: block;
        margin-bottom: 5px;
    }

    .form-group input {
        flex: 2;
        width: 100%;
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
    <h2>Register</h2>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="form-group">
            <label for="firstName">First Name</label>
            <input type="text" id="firstName" bind:value={firstName} required />
        </div>
        <div class="form-group">
            <label for="lastName">Last Name</label>
            <input type="text" id="lastName" bind:value={lastName} required />
        </div>
        <div class="form-group">
            <label for="dob">Date of Birth</label>
            <input type="date" id="dob" bind:value={dateOfBirth} />
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" bind:value={email} required />
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" bind:value={password} required />
        </div>
        <div class="form-group">
            <button type="submit">Register</button>
        </div>
    </form>
</div>