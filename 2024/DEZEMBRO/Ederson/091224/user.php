<?php

session_start();
include ("verificacao.php");


?>
<h5> <?php
echo "nome = ".$_SESSION['nome']."<br>";
echo "setor =".$_SESSION['setor']."<br>";
?></h5>
<a href = "logout.php">Sair</a><br/>




