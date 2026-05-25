<!DOCTYPE html>

<html>

<head>

<title>
Saved Jobs
</title>

<style>

body{

background:#020617;

color:white;

font-family:Poppins;

}

.box{

padding:40px;

}

.card{

background:#1e293b;

padding:30px;

margin-bottom:20px;

border-radius:18px;

}

a{

color:#60a5fa;

}

button{

padding:12px;

background:red;

border:none;

color:white;

border-radius:10px;

}

</style>

</head>

<body>

<div class="box">

<h1>

Saved Jobs

</h1>

<br>

{% for job in saved_jobs %}

<div class="card">

<h2>

{{job[1]}}

</h2>

<p>

{{job[2]}}

</p>

<p>

{{job[3]}}

</p>

<a
href="{{job[4]}}"
>

Open

</a>

<br><br>

<form
action="/delete"
method="POST"
>

<input
type="hidden"
name="id"
value="{{job[0]}}"
>

<button>

Delete

</button>

</form>

</div>

{% endfor %}

</div>

</body>

</html>