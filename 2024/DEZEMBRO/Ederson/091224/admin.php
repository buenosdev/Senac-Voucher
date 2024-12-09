<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<form method="POST" action="action_user.php"><br><br>

    Nome <br><input type="text" name="first_name" id="fn"><br><br>

    Sobrenome <br><input type="text" name="last_name" id="In"><br><br>

    Fone <br><input type="text" name="fone" id="fone"><br><br>

    Endereço <br><input type="text" name="address" id="add"><br><br>

    Email <br><input type="text" name="email" id="email"> <br><br>
    
    sexo <br><input type="text" name="sexo" id="sexo"><br><br>

    <br><input type="submit" name="sub" id=""> 
    
    <a href="logout.php" >Sair</a>

</form>

</body>
</html>

<?php
    session_start();
    include("verificacao.php");
    include("verificacao_admin.php");
?>

