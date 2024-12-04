<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
Text = (nome, Rg, CPF, Endereço)
Number = (idade)
Date = (data)
Checkbox = (preferência época do ano)
Radio = (sexo)
Color = (cor)


<form method = "POST" action = "action_radio.php">
    <fieldset id ="forms">
    <legend>Diga-me sobre vc:</legend>
        <input type="text" name = forms value = "nome">Nome
        <input type="text" name = forms value = "rg">RG
        <input type="text" name = forms value = "cpf">CPF
        <input type="text" name = forms value = "endereco">Endereço
        <input type="number" name = forms value = "idade">Sua idade
        <input type="date" name = forms value = "nascimento">Data de nascimento
    </fieldset>

    <fieldset>
    <legend>Preferência de época do ano</legend>
    <input type="checkbox" name = forms value = "outono">Outono
    <input type="checkbox" name = forms value = "inverno">Inverno
    <input type="checkbox" name = forms value = "primavera">Primavera
    <input type="checkbox" name = forms value = "verao" checked>Verão
    </fieldset>
    

</form>

</body>
</html>