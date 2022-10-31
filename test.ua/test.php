<?php
$current = (int)$_POST['year'];

function getYear($current)
{
    $start = 1;
    if ($current < $start) return "Need > 1";
    return array(
        "Symbol of this year - Chicken",
        "Symbol of this year - Dog",
        "Symbol of this year - Pig",
        "Symbol of this year - Rat",
        "Symbol of this year - Bull",
        "Symbol of this year - Tiger",
        "Symbol of this year - Rabbit",
        "Symbol of this year - Dragon",
        "Symbol of this year - Snake",
        "Symbol of this year - Horse",
        "Symbol of this year - Sheep",
        "Symbol of this year - Monkey"
    )[($current - $start) % 12];
}

$result = getYear($current);
echo "<b>$result</b>";

?>
<form method="POST" action="index.html">
<p><input type="submit" value="Choose another year"></p>