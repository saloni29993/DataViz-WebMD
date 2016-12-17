<?php
   include("simple_html_dom.php");

   $html=file_get_html("http://www.webmd.com/first-aid/default.htm");

   $scraped_data = array();

   foreach ($html->find("div#ContentPane11 ul li") as $a) {
   		$data = strtolower($a->plaintext);
         array_push($scraped_data, $data);
   }

   $file = 'symptoms.txt';
   $str = implode("\n", $scraped_data);
   file_put_contents($file, $str);   
?>
