<!DOCTYPE html>
<html lang="fi">
<head>
    <meta charset="UTF-8">
    <title>LEMP</title>
    <style>
        body { font-family: Arial; text-align:center; margin-top:50px; }
        h1 { font-size: 36px; }
        .btn {
            background-color: #28a745;
            padding: 15px 25px;
            color: white;
            font-size: 18px;
            border-radius: 6px;
            text-decoration: none;
        }
    </style>
</head>
<body>

<h1>Tervetuloa minun LEMP-sivulleni!</h1>

<p>
Palvelimen kellonaika (MySQL):
<b>
<?php
$mysqli = new mysqli("localhost", "stream", "streampass", "testidb");
$result = $mysqli->query("SELECT NOW() AS aika");
$row = $result->fetch_assoc();
echo $row['aika'];
?>
</b>
</p>

<br>

<a class="btn" href="/data-analysis/">Avaa Streamlit-sovellus</a>

<br><br><br>
<p>Tehty CSC:n cPouta-ympäristössä<br>— Oma Nimi —</p>

</body>
</html>
