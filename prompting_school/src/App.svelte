<script>
	//export let name;
	import { Router, Link, Route } from 'svelte-routing';
	import Home from "./routes/Home.svelte";
	import Register from "./routes/Register.svelte"
	import Login from './routes/Login.svelte';
	import Course from './routes/Course.svelte';
	import Lesson1 from './routes/Lesson1.svelte';
	import Profile from './routes/Profile.svelte';
</script>

<main>
	<Router>
		<Route path="/" component={Home} />
		<Route path="register" component={Register} />
		<Route path="course" component={Course} />
		<Route path="login" component={Login} />
		<Route path="lesson1" component={Lesson1} />
		<Route path="profile" component={Profile} />
	</Router>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>