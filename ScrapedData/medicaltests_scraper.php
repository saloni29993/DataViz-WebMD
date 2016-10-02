<?php
   include("simple_html_dom.php");

   $html=file_get_html("http://www.webmd.com/a-to-z-guides/tests/default.htm");
   // $title=$html->find("div#ContentPane11", 0)->plaintext;
   // echo $title;

   $file = 'medicaltests.txt';

   foreach ($html->find("div#a-z-list ul li") as $a) {
   		$scraped_data = $a->plaintext."<br />";
   		echo $scraped_data;
   		file_put_contents($file, $scraped_data);
   }
   
?>
