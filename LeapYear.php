

<form action="" method="POST">
Type a year:
<br><br>
<input type="text" name="number_entered" value=''/> <br><br>
<input type="submit" name="check" value="Leap Year?"/><br><br>
</form>
<?php
$checkbutton= $_POST['check'];
$year= $_POST['number_entered'];

if ($checkbutton){
    if ($year % 100 == 0){
        if ($year % 400){
            echo"It's a leap year!";
        }
        else{
                echo"It's not a leap year!";
            }
    }
    else{
        if ($year % 4 == 0){
            echo "It's a leap year!";
        }
        else{
            echo "It's not a leap year!";
        }
    }
}
?>