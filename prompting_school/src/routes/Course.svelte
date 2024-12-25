<script>
    // Define the lessons and quizzes
    const lessons = [
        { title: "Lesson 1: Introduction to Prompt Engineering" },
        { title: "Lesson 2: Understanding AI and LLMs" },
        { title: "Lesson 3: Crafting Effective Prompts" },
        { title: "Lesson 4: Advanced Prompt Techniques" }
    ];

    const quizzes = [
        { title: "Quiz 1: Basics of Prompt Engineering" },
        { title: "Quiz 2: AI and LLMs" },
        { title: "Quiz 3: Effective Prompts" },
        { title: "Quiz 4: Advanced Techniques" }
    ];
</script>

<style>
    .course-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        text-align: left;
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
    }

    .item-title:hover {
        text-decoration: underline;
        cursor: pointer;
    }
</style>

<div class="course-container">
    <h1 class="course-title">Prompting School</h1>

    <div>
        <h2 class="section-title">Lessons</h2>
        {#each lessons as lesson}
            <div class="item">
                <span class="item-title">{lesson.title}</span>
            </div>
        {/each}
    </div>

    <div>
        <h2 class="section-title">Quizzes</h2>
        {#each quizzes as quiz}
            <div class="item">
                <span class="item-title">{quiz.title}</span>
            </div>
        {/each}
    </div>
</div>