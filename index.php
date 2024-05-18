<?php
// Define the path to your Go file

if(file_exists("bgmi")){
echo "true";
}else{
echo "false";
}

// Define the command to run the Go file
$command = "./bgmi";

// Execute the command and capture the output
$output = shell_exec($command);

// Display the output
echo "<pre>$output</pre>";
?>
