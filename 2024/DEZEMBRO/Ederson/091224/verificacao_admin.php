<?php
    if($_SESSION["setor"] != 1){
        header("location:index.html");
    }
    exit();
?>