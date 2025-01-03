<script>
    import { onMount } from 'svelte';
    let userInfo = {};
    let userProgress = {};

    async function fetchUserInfo() {
        try {
            const token = localStorage.getItem('authToken');
            const response = await fetch('https://api.yourdomain.com/user-info', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            const data = await response.json();
            if (response.ok) {
                userInfo = data.userInfo;
                userProgress = data.userProgress;
            } else {
                console.error('Error fetching user info:', data.error);
            }
        } catch (error) {
            console.error('Error fetching user info:', error);
        }
    }

    onMount(() => {
        fetchUserInfo();
    });
</script>

<style>
    .profile-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f9f9f9;
    }

    .profile-title {
        font-size: 2em;
        margin-bottom: 20px;
        text-align: center;
    }

    .profile-section {
        margin-bottom: 20px;
    }

    .profile-section h3 {
        margin-bottom: 10px;
    }

    .profile-section p {
        margin: 5px 0;
    }
</style>

<div class="profile-container">
    <h1 class="profile-title">Profile</h1>

    <div class="profile-section">
        <h3>User Information</h3>
        <p><strong>First Name:</strong> {userInfo.firstName}</p>
        <p><strong>Last Name:</strong> {userInfo.lastName}</p>
        <p><strong>Email:</strong> {userInfo.email}</p>
    </div>

    <div class="profile-section">
        <h3>Course Progress</h3>
        <p><strong>Lessons Completed:</strong> {userProgress.lessonsCompleted}</p>
        <p><strong>Current Score:</strong> {userProgress.currentScore}</p>
    </div>
</div>