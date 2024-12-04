<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $nome = ($_POST['nome']);
    $rg = ($_POST['rg']);
    $cpf = ($_POST['cpf']);
    $endereco = ($_POST['endereco']);
    $idade = ($_POST['idade']);
    $data_nascimento = ($_POST['data_nascimento']);
    $sexo = isset($_POST['sexo']) ? ($_POST['sexo']) : 'Não informado';
    $preferencias = isset($_POST['preferencia']) ? $_POST['preferencia'] : [];
    $cor_preferida = ($_POST['cor_preferida']);

    echo "<table border='1'>";
    echo "<tr><th>Campo</th><th>Valor</th></tr>";
    echo "<tr><td>Nome</td><td>$nome</td></tr>";
    echo "<tr><td>RG</td><td>$rg</td></tr>";
    echo "<tr><td>CPF</td><td>$cpf</td></tr>";
    echo "<tr><td>Endereço</td><td>$endereco</td></tr>";
    echo "<tr><td>Idade</td><td>$idade</td></tr>";
    echo "<tr><td>Data de Nascimento</td><td>$data_nascimento</td></tr>";
    echo "<tr><td>Sexo</td><td>$sexo</td></tr>";
    echo "<tr><td>Preferências de Época</td><td>" . implode(', ', $preferencias) . "</td></tr>";
    echo "<tr><td>Cor Preferida</td><td><div style='width:20px; height:20px; background-color:$cor_preferida;'></div></td></tr>";
    echo "</table>";
} else {
    echo "<p>Os dados não foram enviados pelo método POST.</p>";
}
?>
