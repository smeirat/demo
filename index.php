<?php

$method = $_SERVER['REQUEST_METHOD'];
if($method == "POST"){
$requestBody = file_get_contents('php://input');
$json = json_decode($requestBody);

$text = $json->result->parameters->text;

switch ($text) {
	case 'hi':
		$speech = "Hi hussam, nice to meet you bro";
		break;
	
    case 'bye'
    $speech = "bye, have a good day";
    break;

        case 'anything'
    $speech = "yes you can type anything";
    break;


	default:
		 $speech = "Sorry, i didnt get that";
		break;
}

$response = new \StdClass();
$response->speech = "";
$response->displayText = "";
$response->source = "webhook";
echo json_encode($response);
}
else
{
echo "Method not allowed";
}

?>