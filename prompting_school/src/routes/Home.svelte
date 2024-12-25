<script>
    // Add any JavaScript you need here
    import {Link} from 'svelte-routing';
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

    .title {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        text-align: left;
        flex-grow: 1;
    }

    .buttons {
        /* What display: options are there */
        display: flex
    }

    .button {
        background-color: #007BFF;
        color: white;
        padding: 10px 40px;
        margin: 5px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px; 
    }
    
    .button:hover {
        background-color: #0056b3;
    }

    .container {
        flex: 1;
        max-width: 800px;
        margin: 0 auto;
        padding: 100px 20px 20px; /* Adjust for fixed header */
        text-align: center;
    }

    h2 {
        color: #333;
        margin-bottom: 20px;
    }

    p {
        color: #666;
        font-size: 18px;
        line-height: 1.6;
        text-align: left;
    }

    .start-course {
        margin-top: 30px;
    }

    .start-course .button {
        background-color: #28a745;
        color: white;
        padding: 10px 20px;
        margin: 5px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }

    .start-course .button:hover {
        background-color: #218838;
    }

    .footer {
        background-color: #fff;
        padding: 20px;
        text-align: center;
        box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
    }

    .footer p {
        color: #666;
        font-size: 16px;
        margin: 5px 0;
    }
</style>

<div class="header">
    <div class="title">Prompting School</div>
    <div class="buttons">
        <button class="button">Log In</button>
        <Link to="register" class="button-link">
            <button class="button">Register</button>
        </Link>

    </div>
</div>

<div class="container">
    <h2>Welcome to Prompting School</h2>
    <div>
        <p>Welcome to Prompting School, your ultimate destination for mastering the art of prompt engineering. This course is designed to equip you with the skills and knowledge needed to excel in creating effective prompts for AI models.</p>
        <p>Whether you are a beginner or an experienced professional, our comprehensive curriculum will guide you through the intricacies of prompt engineering, ensuring you gain a deep understanding of the subject.</p>
        <p>Artificial Intelligence (AI) is transforming industries and creating new opportunities. At the heart of AI is the ability to understand and generate human-like text, which is where prompt engineering comes in. By mastering prompt engineering, you can harness the power of AI to create more effective and efficient solutions.</p>
        <p>Large Language Models (LLMs) like GPT-3 have revolutionized the field of AI by enabling machines to understand and generate text with unprecedented accuracy. Learning how to create effective prompts for these models is a crucial skill for anyone looking to leverage AI in their work.</p>
        <p>Our course covers everything from the basics of prompt engineering to advanced techniques for optimizing prompts for different use cases. You'll learn how to create prompts that generate high-quality text, improve model performance, and solve real-world problems.</p>
        <p>Join us at Prompting School and take the first step towards becoming an expert in prompt engineering. Our experienced instructors and comprehensive curriculum will provide you with the knowledge and skills you need to succeed in this exciting field.</p>
    </div>
    <div class="start-course">
        <Link to="course" class="button-link">
            <button class="button">Start Course</button>
        </Link>
    </div>
</div>

<div class="footer">
    <p>Contact: irfanj7@gmail.com</p>
    <p>&copy; 2024 Prompting School. All rights reserved.</p>
</div>