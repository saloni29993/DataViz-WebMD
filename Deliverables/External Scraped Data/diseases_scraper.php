<?php
   include("simple_html_dom.php");

   $base_url=file_get_html("http://www.mayoclinic.org/diseases-conditions/index?letter=A");

   $furl=array();

   foreach($base_url->find("div.holder ol li a") as $url){
      $newurl=$url->href;
      $purl="http://www.mayoclinic.org".$newurl;
      array_push($furl,$purl);
   }

   print_r($furl);

   $scraped_data = array();

   foreach ($furl as $key) {
      {
         $newkey=file_get_html($key);
         foreach($newkey->find("div#index ol li") as $a){
            $data = strtolower($a->plaintext);
            array_push($scraped_data, $data);
         }
      }
   }
   $file="diseases.txt";
   $str = implode("\n", $scraped_data);
   file_put_contents($file, $str);   
?>
