<?php
   include("simple_html_dom.php");

   $html=file_get_html("https://en.wikipedia.org/wiki/List_of_medical_symptoms");

   $scraped_data = array();

   foreach ($html->find("table.wikitable li a") as $a) {
   		$data = strtolower($a->plaintext);
         array_push($scraped_data, $data);
   }

   $file = 'general-symptoms.txt';
   $str = implode("\n", $scraped_data);
   file_put_contents($file, $str);   
?>
