<script>
    import axios from 'axios';
    let inputText = '';
    let result = '';
    let selectedOption = '';
    let mcqResult = '';

    async function handleSubmit() {
        try {
            const response = await axios.post('http://localhost:5000/process', { input_text: inputText });
            result = response.data.result;
        } catch (error) {
            console.error('Error processing input:', error);
        }
    }

    function handleMCQSubmit() {
        if (selectedOption) {
            mcqResult = `You selected option ${selectedOption}`;
        } else {
            mcqResult = 'Please select an option.';
        }
    }
</script>

<style>

    .lesson-title {
        font-size: 2em;
        margin-bottom: 20px;
        text-align: center;
    }

    .lesson-content {
        font-size: 1.2em;
        line-height: 1.6;
    }

    .mcq-container {
        margin-top: 20px;
    }

    .mcq-option {
        margin: 10px 0;
    }

    .mcq-result {
        margin-top: 20px;
        font-weight: bold;
    }
</style>

<div class="lesson-container">
    <h1 class="lesson-title">Lesson 1: Write Clear Instructions</h1>
    <div class="lesson-content">
        <p>Welcome to Lesson 1. In this lesson, you will learn how to write clear and effective instructions for AI models.</p>
        <div class="form-group">
            <label for="inputText">Enter your text:</label>
            <input type="text" id="inputText" bind:value={inputText} />
        </div>
        <div class="form-group">
            <button on:click={handleSubmit}>Submit</button>
        </div>
        {#if result}
            <div class="result">{result}</div>
        {/if}
    </div>

    <div class="mcq-container">
        <h2>BRUSKO</h2>
        <div class="mcq-option">
            <input type="radio" id="optionA" name="mcq" value="A" bind:group={selectedOption} />
            <label for="optionA">Option A</label>
        </div>
        <div class="mcq-option">
            <input type="radio" id="optionB" name="mcq" value="B" bind:group={selectedOption} />
            <label for="optionB">Option B</label>
        </div>
        <div class="mcq-option">
            <input type="radio" id="optionC" name="mcq" value="C" bind:group={selectedOption} />
            <label for="optionC">Option C</label>
        </div>
        <button on:click={handleMCQSubmit}>Submit Answer</button>
        <p class="mcq-result">{mcqResult}</p>
    </div>
</div>