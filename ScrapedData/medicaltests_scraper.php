<?php
   include("simple_html_dom.php");

   $base_url=file_get_html("http://www.webmd.com/a-to-z-guides/tests/default.htm");

   $furl=array();

   foreach($base_url->find("div#a-z-alpha ul li a") as $url){
      $newurl=$url->href;
      $purl="http://www.webmd.com".$newurl;
      array_push($furl,$purl);
   }
   
   $scraped_data=array();

   foreach ($furl as $key) {
      {
         $newkey=file_get_html($key);
         foreach($newkey->find("div#a-z-list ul li") as $a){
            $data = strtolower($a->plaintext);
            array_push($scraped_data, $data);
         }
      }
   }
   $file="medicaltests.txt";
   $str = implode("\n", $scraped_data);
   file_put_contents($file, $str);

?>
