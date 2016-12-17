<?php
   include("simple_html_dom.php");

   $base_url=file_get_html("http://www.webmd.com/drugs/index-drugs.aspx?show=drugs");

   $furl=array();

   foreach($base_url->find("div#drugs- ul#drugs_view li a") as $url){
      $newurl=$url->href;
      $purl="https://www.webmd.com".$newurl;
      array_push($furl,$purl);
   }
   
   $scraped_data=array();

   foreach ($furl as $key) {
      {
         $newkey=file_get_html($key);
         foreach($newkey->find("div#az-content ul li p") as $a){
            $data = strtolower($a->plaintext);
            array_push($scraped_data, $data);
         }
      }
   }
   $file="drugs.txt";
   $str = implode("\n", $scraped_data);
   file_put_contents($file, $str);

?>
