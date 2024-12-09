<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário</title>
</head>
<body>

<form method="POST" action="action.php">
    <fieldset>
        <legend>Diga-me sobre você:</legend>
        <br>
        Nome: <input type="text" name="nome" placeholder="Ex.: João"><br><br>
        RG: <input type="text" name="rg" placeholder="Ex.: 5465465465465"><br><br>
        CPF: <input type="text" name="cpf" placeholder="Ex.: 0926546654654"><br><br>
        Endereço: <input type="text" name="endereco" placeholder="Ex.: Rua do Parque 75"><br><br>
        Sua idade: <input type="number" name="idade" placeholder="Ex.: 17"><br><br>
        Data de nascimento: <input type="date" name="data_nascimento"><br><br>
        Sexo: 
        <input type="radio" name="sexo" value="Masculino"> Masculino
        <input type="radio" name="sexo" value="Feminino"> Feminino
        <input type="radio" name="sexo" value="Outro"> Outro<br><br>
    </fieldset>
    <br>
    <fieldset>
        <legend>Perguntas não obrigatórias</legend>
        <p>Preferência de época do ano:</p>
        <input type="checkbox" name="preferencia[]" value="Outono"> Outono
        <input type="checkbox" name="preferencia[]" value="Inverno"> Inverno
        <input type="checkbox" name="preferencia[]" value="Primavera"> Primavera
        <input type="checkbox" name="preferencia[]" value="Verão"> Verão
        <p>Sua cor preferida:</p>
        Cor: <input type="color" name="cor_preferida"> 
    </fieldset>
    <br>
    <input type="submit" value="Enviar">
</form>

</body>
</html>
