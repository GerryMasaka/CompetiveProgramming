<?php


function gradingStudents($grades) {
    // Write your code here
  for ($i = 0; $i < count($grades); $i++) {
    if ($grades[$i] >= 38) { 
      $x = $grades[$i] % 5;
      if ($x == 3) {
        $grades[$i] += 2;
      } 
      if ($x == 4) {
        $grades[$i] += 1;
      }
    } 
  }
  return $grades;
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$grades_count = intval(trim(fgets(STDIN)));

$grades = array();

for ($i = 0; $i < $grades_count; $i++) {
    $grades_item = intval(trim(fgets(STDIN)));
    $grades[] = $grades_item;
}

$result = gradingStudents($grades);

fwrite($fptr, implode("\n", $result) . "\n");

fclose($fptr);
