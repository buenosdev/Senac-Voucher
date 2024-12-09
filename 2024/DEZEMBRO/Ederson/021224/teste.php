<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<!-- <?php

    for ($contador = 0; $contador < 10; $contador++) {
        echo "Hello World! " . ($contador + 1); 
        echo "<br>";
    }
?> -->

<form method = "GET" action = "action.php">
    <fieldset id ="pessoal">
        <legend>Dados pessoais</legend>
        <p> Nome <input type = "text" name = "nome" id = "nome" size ="20" maxlength="20" placeholder = "Ex.:João"></p>
    </fieldset>
    <br>
</form>

<form method = "POST" action = "action_radio.php">
    <fieldset id ="sistema">
    <legend>Qual seu sistema?</legend>
        <input type="radio" name = sistema value = "Windows98">Win98
        <input type="radio" name = sistema value = "WindowsXP">WinXP
        <input type="radio" name = sistema value = "Outros" checked> Outros
    </fieldset>
    <br>

</form>

<form method = "POST" action = "action_check.php">
    <fieldset id ="pior">
    <legend>Qual o professor?</legend>
        <input type="checkbox" id = "ederson" name = "prof[]" value = "Ederson" checked>
        <label for="ederson">Ederson</label>
        <input type="checkbox" id = "horns" name = "prof[]" value = "Ederson da Costa">
        <label for="Ederson costa">Ederson Costa</label>
    </fieldset>
    <br>
<input type = "submit" value = "Enviar">
</form>

</body>
</html>



<!-- html:5>php>echo.text*5 -->
<!-- ul>li.item$*5 -->
