<script>
    import { Link, navigate } from 'svelte-routing';
    import { onMount } from 'svelte';

    // Define the lessons and quizzes
    const lessons = [
        { title: "Lesson 1: Write Clear Instructions", path: "lesson1" },
        { title: "Lesson 2: Provide reference text" },
        { title: "Lesson 3: Split complex tasks into simpler subtasks" },
        { title: "Lesson 4: Give models time to think" },
        { title: "Lesson 5: Use external tools" },
        { title: "Lesson 6: Test changes systematically"}
        
    ];

    let showDropdown = false;

    function toggleDropdown() {
        showDropdown = !showDropdown;
    }

    function goToProfile() {
        navigate('/profile');
    }

    function logOut() {
        // Perform logout logic here
        console.log('User logged out');
        navigate('/login');
    }

    onMount(() => {
        // Check if the user is authenticated
        const token = localStorage.getItem('authToken');
        if (!token) {
            // If not authenticated, redirect to login page
            navigate('/login');
        }
    });
</script>

<style>
    .header {
        position: fixed;
        top: 0;
        left: 0; 
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        box-sizing: border-box; /* Includes padding in width/height calculations */
    }

    .course-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        text-align: left;
        margin-top: 60px; /* Add margin to avoid overlap with fixed header */
    }

    .course-title {
        font-size: 2em;
        margin-bottom: 20px;
        text-align: center;
    }

    .section-title {
        font-size: 1.5em;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .item {
        margin-bottom: 10px;
    }

    .item-title {
        font-size: 1.2em;
        color: #007BFF;
        text-decoration: none;
    }

    .item-title:hover {
        text-decoration: underline;
        cursor: pointer;
    }

    .profile-button {
        position: relative;
        cursor: pointer;
    }

    .dropdown-menu {
        position: absolute;
        right: 0;
        top: 100%;
        background-color: #fff;
        border: 1px solid #ccc;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        z-index: 1001;
        display: none;
    }

    .dropdown-menu.show {
        display: block;
    }

    .dropdown-item {
        padding: 10px 20px;
        cursor: pointer;
    }

    .dropdown-item:hover {
        background-color: #f1f1f1;
    }
</style>

<div class="header">
    <div class="title">Prompting School</div>
    <div class="profile-button" on:click={toggleDropdown}>
        My Profile
        <div class="dropdown-menu {showDropdown ? 'show' : ''}">
            <div class="dropdown-item" on:click={goToProfile}>Profile</div>
            <div class="dropdown-item" on:click={logOut}>Log Out</div>
        </div>
    </div>
</div>

<div class="course-container">
    <h1 class="course-title">Prompting School</h1>

    <div>
        <h2 class="section-title">Lessons</h2>
        {#each lessons as lesson}
            <div class="item">
                {#if lesson.path}
                    <Link to={lesson.path} class="item-title">{lesson.title}</Link>
                {:else}
                    <span class="item-title">{lesson.title}</span>
                {/if}
            </div>
        {/each}
    </div>
</div>