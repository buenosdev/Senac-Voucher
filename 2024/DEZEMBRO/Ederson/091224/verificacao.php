
<?php
    if(!$_SESSION["name"]){
        header("location:index.html");
    }
    exit();
?>