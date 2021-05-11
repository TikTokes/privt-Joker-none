<?php 
// BY BRoK - @x_BRK - @i_BRK //
ob_start();
define('API_KEY','Token1503102686:AAFdvb-olTLF5ekIe8wlAc8sIPNaq6aJjBA'); // Your Token //
echo file_get_contents("https://api.telegram.org/bot".API_KEY."/setwebhook?url=".$_SERVER['SERVER_NAME']."".$_SERVER['SCRIPT_NAME']);
function bot($method,$datas=[]){$x_BRK = http_build_query($datas);
$url = "https://api.telegram.org/bot".API_KEY."/".$method."?$x_BRK";
$i_BRK = file_get_contents($url); return json_decode($i_BRK);}
$update = json_decode(file_get_contents('php://input'));
$message = $update->message; $chat_id = $message->chat->id;
$from_id = $message->from->id; $name = $message->from->first_name; $text = $message->text;
$mid = $message->message_id; $name2 = $update->callback_query->from->first_name; $message_id2 = $update->callback_query->message->message_id; $chat_id2 = $update->callback_query->message->chat->id;
$from_id2 = $update->callback_query->from->id; $message_id = $update->callback_query->message->message_id; $data = $update->callback_query->data;
$info_token = file_get_contents("https://api.telegram.org/bot$text/getWebhookInfo"); $info_tokens = json_decode($info_token);
// bots files - BY BRoK @x_BRK - @i_BRK //
$get_hms = file_get_contents('hms.php');
$get_down = file_get_contents('Down.php');
$get_twsl = file_get_contents('Twsl.php');
$get_sayt= file_get_contents('Sayt.php');
$get_zkrf = file_get_contents('Zkrf.php');
$get_buy = file_get_contents('buy.php');
$get_convert = file_get_contents('convert.php');
$get_flan = file_get_contents('flan.php');
$get_khera = file_get_contents('khera.php');
$get_safech = file_get_contents('safech.php');
$get_markdown = file_get_contents('markdown.php');
$get_sixth = file_get_contents('sixth.php');
// Get Explode INFO - BY BRoK @x_BRK - @i_BRK //
$get_done_down = file_get_contents('infos/explodedownload.php');
$done_down = explode("\n", $get_done_down);
$get_done_hms = file_get_contents('infos/explodehms.php');
$done_hms = explode("\n",$get_done_hms);
$get_done_sayt = file_get_contents('infos/explodesayt.php');
$done_sayt = explode("\n", $get_done_sayt);
$get_done_twsl= file_get_contents('infos/explodetwsl.php');
$done_twsl = explode("\n", $get_done_twsl);
$get_done_zkrf = file_get_contents('infos/explodezkrf.php');
$done_zkrf = explode("\n", $get_done_zkrf);
$get_done_buy = file_get_contents('infos/explodebuy.php');
$done_buy = explode("\n", $get_done_buy);
$get_done_convert = file_get_contents('infos/explodeconvert.php');
$done_convert = explode("\n",$get_done_convert);
$get_done_flan = file_get_contents('infos/explodeflan.php');
$done_flan = explode("\n", $get_done_flan);
$get_done_khera = file_get_contents('infos/explodekhera.php');
$done_khera = explode("\n", $get_done_khera);
$get_done_safech = file_get_contents('infos/explodesafech.php');
$done_safech = explode("\n", $get_done_safech);
$get_done_markdown = file_get_contents('infos/explodemarkdown.php');
$done_markdown = explode("\n", $get_done_markdown);
$get_done_sixth = file_get_contents('infos/explodesixth.php');
$done_sixth = explode("\n", $get_done_sixth);
$get_id = file_get_contents('infos/info.php'); 
$get_ids = explode("\n", $get_id);
$from_id = $message->from->id;
mkdir("infos");
mkdir("$from_id");
// BRoK INFO - @x_BRK - @i_BRK //
$index="<html>
<meta HTTP-EQUIV='REFRESH' content='0; url=https://t.me/i_BRK'/>
</html>";
$admin = 610569681; // Sudo ID //
$urls="https://name.domain/Maker"; // Website Link //
// Sudo Orders - BY BRoK - @x_BRK - @i_BRK //
$i_BRK = $admin; 
$x_BRK = file_get_contents("x_BRK.txt");
$x_BRK0 = file_get_contents("x_BRK0.txt");
$x_BRK1= file_get_contents("x_BRK1.txt");
$x_BRK5 = file_get_contents("x_BRK2.txt");
$x_BRK6 = file_get_contents("x_BRK3.txt");
$x_BRK20 = json_decode(file_get_contents('php://input'));
$x_BRK18 = $update->message;
$chat_id = $x_BRK18->chat->id;
$text = $x_BRK18->text;
$data = $x_BRK20->callback_query->data;
$x_BRK12 = $x_BRK20->callback_query->message->chat->id;
$x_BRK14 =  $x_BRK20->callback_query->message->message_id;
$x_BRK15 = $x_BRK18->from->first_name;
$x_BRK16 = $x_BRK18->from->username;
$x_BRK11 = $x_BRK18->from->id;
$x_BRK2 = explode("\n",file_get_contents("x_BRK4.txt"));
$x_BRK3 = count($x_BRK2)-1;
if ($x_BRK18 && !in_array($x_BRK11, $x_BRK2)) {
    file_put_contents("x_BRK4.txt", $x_BRK11."\n",FILE_APPEND);
  }
$x_BRK9 = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=$x_BRK0&user_id=".$x_BRK11);
$x_BRK10 = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=$x_BRK1&user_id=".$x_BRK11);
if($x_BRK18 && (strpos($x_BRK9,'"status":"left"') or strpos($x_BRK9,'"Bad Request: USER_ID_INVALID"') or strpos($x_BRK9,'"status":"kicked"') or strpos($x_BRK10,'"status":"left"') or strpos($x_BRK10,'"Bad Request: USER_ID_INVALID"') or strpos($x_BRK10,'"status":"kicked"'))!== false){
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>"- عذرا عزيزي يجب عليك الاشتراك في قناة البوت اولا

$x_BRK0
$x_BRK1",
]);return false;}
if($text == "/start" and $x_BRK11 == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>'- اهلا بك في قائمة اوامر الادمن',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'- قناة الاشتراك الاجباري الاولى' ,'callback_data'=>"x_BRK"]],
[['text'=>'- وضع قناة' ,'callback_data'=>"x_BRK0"],['text'=>'- حذف قناة' ,'callback_data'=>"x_BRK1"]],
[['text'=>'قناة الاشتراك الاجباري الثانيه' ,'callback_data'=>"x_BRK"]],
[['text'=>'- وضع قناة' ,'callback_data'=>"x_BRK2"],['text'=>'- حذف قناة' ,'callback_data'=>"x_BRK3"]],
[['text'=>'- - عرض قنوات الاشتراك الاجباري' ,'callback_data'=>"x_BRK4"]],
[['text'=>'- قائمة الاذاعه' ,'callback_data'=>"x_BRK"]],
[['text'=>'- اذاعه بلتوجيه' ,'callback_data'=>"x_BRK5"],['text'=>'- اذاعة نص' ,'callback_data'=>"x_BRK6"]],
[['text'=>'- عدد المشتركين' ,'callback_data'=>"x_BRK7"]],
[['text'=>'- التواصل' ,'callback_data'=>"x_BRK"]],
[['text'=>'- تفعيل التواصل' ,'callback_data'=>"x_BRK11"],['text'=>'- تعطيل التواصل' ,'callback_data'=>"x_BRK12"]],
[['text'=>'- احصائيات البوت', 'callback_data'=>"status"]], 
   ] 
   ])
]);
}
if($data == "x_BRK" ){
bot('EditMessageText',[
'chat_id'=>$x_BRK12,
'message_id'=>$x_BRK14,
"text"=>'- اهلا بك في قائمة اوامر الادمن',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'- قناة الاشتراك الاجباري الاولى' ,'callback_data'=>"x_BRK"]],
[['text'=>'- وضع قناة' ,'callback_data'=>"x_BRK0"],['text'=>'- حذف قناة' ,'callback_data'=>"x_BRK1"]],
[['text'=>'قناة الاشتراك الاجباري الثانيه' ,'callback_data'=>"x_BRK"]],
[['text'=>'- وضع قناة' ,'callback_data'=>"x_BRK2"],['text'=>'- حذف قناة' ,'callback_data'=>"x_BRK3"]],
[['text'=>'- - عرض قنوات الاشتراك الاجباري' ,'callback_data'=>"x_BRK4"]],
[['text'=>'- قائمة الاذاعه' ,'callback_data'=>"x_BRK"]],
[['text'=>'- اذاعه بلتوجيه' ,'callback_data'=>"x_BRK5"],['text'=>'- اذاعة نص' ,'callback_data'=>"x_BRK6"]],
[['text'=>'- عدد المشتركين' ,'callback_data'=>"x_BRK7"]],
[['text'=>'- التواصل' ,'callback_data'=>"x_BRK"]],
[['text'=>'- تفعيل التواصل' ,'callback_data'=>"x_BRK11"],['text'=>'- تعطيل التواصل' ,'callback_data'=>"x_BRK12"]],
[['text'=>'- احصائيات البوت', 'callback_data'=>"status"]], 
   ] 
   ])
]);
unlink("x_BRK.txt");
}
if($data == "x_BRK0"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>'- ارسل معرف القناة الاولى',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- الغاء' ,'callback_data'=>"x_BRK"]],
]])
]);
file_put_contents("x_BRK.txt","x_BRK0");
}
if($text and $x_BRK == "x_BRK0" and $x_BRK11 == $i_BRK){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"- تم حفظ $text كقناة اولى للاشتراك الاجباري
- تأكد من رفع البوت ادمن بلقناة" ,
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
file_put_contents("x_BRK0.txt","$text");
unlink("x_BRK.txt");
}
if($data == "x_BRK1"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>'- تم حذف القناة الاولى',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
unlink("x_BRK.txt");
unlink("x_BRK0.txt");
}
if($data == "x_BRK2"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>'- ارسل معرف القناة الثانيه',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- الغاء' ,'callback_data'=>"x_BRK"]],
]])
]);
file_put_contents("x_BRK.txt","x_BRK1");
}
if($text and $x_BRK == "x_BRK1" and $x_BRK11 == $i_BRK){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"- تم حفظ $text كقناة ثانيه للاشتراك الاجباري
- تأكد من رفع البوت ادمن بلقناة" ,
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
file_put_contents("x_BRK1.txt","$text");
unlink("x_BRK.txt");
}
if($data == "x_BRK3"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>'- تم حذف القناة الثانيه',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
unlink("x_BRK.txt");
unlink("x_BRK1.txt");
}
if($data == "x_BRK4"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>"- هذه هي قائمة قنوات الاتشراك الاجباري
1 => $x_BRK0
- - - - - 
2 => $x_BRK1",
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
unlink("x_BRK.txt");
}
if($data == "x_BRK5"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>'- ارسل الرساله ليتم توجيهها لجميع المشتركين',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- الغاء' ,'callback_data'=>"x_BRK"]],
]])
]);
file_put_contents("x_BRK.txt","x_BRK2");
}
if($x_BRK18 and $x_BRK == "x_BRK2" and $x_BRK11 == $i_BRK){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"- تم توجيه الرساله ل$x_BRK3 مشترك",
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
for($i=0;$i<count($x_BRK2); $i++){
bot('forwardMessage', [
'chat_id'=>$x_BRK2[$i],
'from_chat_id'=>$x_BRK11,
'message_id'=>$x_BRK18->message_id
]);
unlink("x_BRK.txt");
}
}
if($data == "x_BRK6"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>'- ارسل النص الان ليتم نشره لجميع المشتركين',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- الغاء' ,'callback_data'=>"x_BRK"]],
]])
]);
file_put_contents("x_BRK.txt","x_BRK3");
}
if($text and $x_BRK == "x_BRK3" and $x_BRK11 == $i_BRK){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"- تم نشر رسالتك ل$x_BRK3 مشترك" ,
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
for($i=0;$i<count($x_BRK2); $i++){
bot('sendMessage', [
'chat_id'=>$x_BRK2[$i],
'text'=>$text
]);
unlink("x_BRK.txt");
}
}
if($data == "x_BRK7"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>"- عدد مشتركين البوت $x_BRK3",
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
unlink("x_BRK.txt");
}
if($data == "x_BRK11"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>'- تم تفعيل التواصل',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
file_put_contents("x_BRK3.txt","x_BRK");
}
if($x_BRK18 and $x_BRK6 == "x_BRK" and $x_BRK11 != $i_BRK){
bot('forwardMessage', [
'chat_id'=>$i_BRK,
'from_chat_id'=>$x_BRK11,
'message_id'=>$x_BRK18->message_id
]);
}
if($x_BRK18 and $x_BRK6 == "x_BRK" and $x_BRK11 == $i_BRK){
bot('sendMessage',[
'chat_id'=>$x_BRK18->reply_to_message->forward_from->id,
    'text'=>$text,
    ]);
}
if($data == "x_BRK12"){
bot('EditMessageText',[
    'chat_id'=>$x_BRK12,
    'message_id'=>$x_BRK14,
'text'=>'- تم تعطيل التواصل',
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
unlink("x_BRK.txt");
unlink("x_BRK3.txt");
}
if($text == '/start'){ bot('sendMessage',[
'chat_id'=>$chat_id,'text'=>"
- اهلا بك عزيزي في بوت مصنع بوتات التليكرام
- اضغط على اصنع بوت واصنع البوت الخاص بك الان مجانا!
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,'reply_markup'=>json_encode(['inline_keyboard'=>[[['text'=>'- اصنع بوت','callback_data'=>'makebot']],],])]);}
if($data == 'makebot'){ bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"- قم بأرسال التوكن الخاص بك\n- يمكنك الحصول عليه من @BotFather",'reply_markup'=>json_encode(['inline_keyboard'=>[[['text'=>'- كيفية صنع بوت','callback_data'=>'howmakebrok']],[['text'=>'- رجوع','callback_data'=>'Back']],]])]);}
if($data == 'howmakebrok'){
       bot('sendvideo',[
 'chat_id'=>$chat_id2,
 'video'=>"https://t.me/brokmakebots/2",
 'caption'=>"- هذا هو شرح كيفية صنع بوت خاص بك",
 ]);
}
if($text and $info_tokens->ok == "true" ){
mkdir("$from_id");
mkdir("$from_id/Down");
mkdir("$from_id/Hms");
mkdir("$from_id/Twsl");
mkdir("$from_id/Sayt");
mkdir("$from_id/Zkrf");
mkdir("$from_id/buy");
mkdir("$from_id/convert");
mkdir("$from_id/flan");
mkdir("$from_id/khera");
mkdir("$from_id/safech");
mkdir("$from_id/markdown");
mkdir("$from_id/sixth");
file_put_contents("$from_id/Token.php","$text");
$str = str_replace($from_id, '', $get_id);
file_put_contents('infos/info.php', $str);    
bot('sendMessage',['chat_id'=>$chat_id,'text'=>"
- اختر البوت الذي تريد صنعه الان 
- ملاحضه : يمكنك صنع بوت واحد فقط من كل نوع
",
'reply_markup'=>json_encode(['inline_keyboard'=>[
[['text'=>'- تحميل من الانستا + الفيس','callback_data'=>"Down"],['text'=>'- تواصل','callback_data'=>'Twsl']],
[['text'=>'- همسه','callback_data'=>"Hms"],['text'=>'- بوت متجر','callback_data'=>"buy"]],
[['text'=>'- سايت','callback_data'=>"Sayt"],['text'=>'- زخرفه','callback_data'=>'Zkrf']],
[['text'=>'- تحويل صيغ','callback_data'=>"convert"],['text'=>'- شنو رأيك بفلان','callback_data'=>'flan']],
[['text'=>'- خيره','callback_data'=>"khera"],['text'=>'- حماية قنوات','callback_data'=>'safech']],
[['text'=>'- صنع ازرار شفافه','callback_data'=>"markdown"],['text'=>'- مكتبة السادس','callback_data'=>'sixth']],
]])]);}
if($data == 'Down' and in_array($chat_id2,$done_down)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت تحميل من الفيس + الانستا من قبل!
",
]);
}
if($data == 'Down' and !in_array($chat_id2,$done_down)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/Down/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/Down/Down.php","$get_down");
file_put_contents("$chat_id2/Down/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/Down/Down.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodedwonload.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت تحميل من الفيس + الانستا خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'Hms' and in_array($chat_id2,$done_hms)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت همسه من قبل!
",
]);
}
if($data == 'Hms' and !in_array($chat_id2,$done_hms)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/Hms/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/Hms/Hms.php","$get_hms");
file_put_contents("$chat_id2/Hms/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/Hms/Hms.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodehms.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت همسه خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'Twsl' and in_array($chat_id2,$done_twsl)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت تواصل من قبل!
",
]);
}
if($data == 'Twsl' and !in_array($chat_id2,$done_twsl)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/Twsl/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/Twsl/Twsl.php","$get_twsl");
file_put_contents("$chat_id2/Twsl/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/Twsl/Twsl.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodetwsl.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت تواصل خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'Sayt' and in_array($chat_id2,$done_sayt)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت سايت من قبل!
",
]);
}
if($data == 'Sayt' and !in_array($chat_id2,$done_sayt)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/Sayt/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/Sayt/Sayt.php","$get_sayt");
file_put_contents("$chat_id2/Sayt/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/Sayt/Sayt.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodesayt.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت سايت خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'Zkrf' and in_array($chat_id2,$done_zkrf)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت زخرفه من قبل!
",
]);
}
if($data == 'Zkrf' and !in_array($chat_id2,$done_zkrf)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/Zkrf/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/Zkrf/Zkrf.php","$get_zkrf");
file_put_contents("$chat_id2/Zkrf/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/Zkrf/Zkrf.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodezkrf.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت زخرفه خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'buy' and in_array($chat_id2,$done_buy)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت متجر من قبل!
",
]);
}
if($data == 'buy' and !in_array($chat_id2,$done_buy)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/buy/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/buy/buy.php","$get_buy");
file_put_contents("$chat_id2/buy/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/buy/buy.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodebuy.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت متجر خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'convert' and in_array($chat_id2,$done_convert)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت تحويل صيغ من قبل!
",
]);
}
if($data == 'convert' and !in_array($chat_id2,$done_convert)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/convert/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/convert/convert.php","$get_convert");
file_put_contents("$chat_id2/convert/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/convert/convert.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodeconvert.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت تحويل صيغ خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'flan' and in_array($chat_id2,$done_flan)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت شنو رأيك بفلان من قبل!
",
]);
}
if($data == 'flan' and !in_array($chat_id2,$done_flan)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/flan/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/flan/flan.php","$get_flan");
file_put_contents("$chat_id2/flan/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/flan/flan.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodeflan.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت شنو رأيك بفلان خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'khera' and in_array($chat_id2,$done_khera)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت خيره من قبل!
",
]);
}
if($data == 'khera' and !in_array($chat_id2,$done_khera)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/khera/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/khera/khera.php","$get_khera");
file_put_contents("$chat_id2/khera/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/khera/khera.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodekhera.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت خيره خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'safech' and in_array($chat_id2,$done_safech)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت حماية قنوات من قبل!
",
]);
}
if($data == 'safech' and !in_array($chat_id2,$done_safech)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/safech/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/safech/safech.php","$get_safech");
file_put_contents("$chat_id2/safech/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/safech/safech.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodesafech.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت حماية قنوات خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'markdown' and in_array($chat_id2,$done_markdown)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت صنع ازرار شفافه من قبل!
",
]);
}
if($data == 'markdown' and !in_array($chat_id2,$done_markdown)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/markdown/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/markdown/markdown.php","$get_markdown");
file_put_contents("$chat_id2/markdown/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/markdown/markdown.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodemarkdown.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت صنع ازرار شفافه خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'sixth' and in_array($chat_id2,$done_sixth)){
bot('sendMessage',['chat_id'=>$chat_id2,'text'=>"
- لقد قمت بأنشاء بوت مكتبة السادس من قبل!
",
]);
}
if($data == 'sixth' and !in_array($chat_id2,$done_sixth)){
$Token = file_get_contents("$chat_id2/Token.php");
file_put_contents("$chat_id2/sixth/info.php","$Token\n$chat_id2");
file_put_contents("$chat_id2/sixth/sixth.php","$get_sixth");
file_put_contents("$chat_id2/sixth/index.html","$index");
file_put_contents("$chat_id2/index.html","$index");
file_get_contents("https://api.telegram.org/bot$Token/setwebhook?url=$urls/$chat_id2/sixth/sixth.php");
$url_info = file_get_contents("https://api.telegram.org/bot$Token/getMe");
$json_info = json_decode($url_info);
$userr = $json_info->result->username;
file_put_contents('infos/explodesixth.php', $chat_id2 . "\n", FILE_APPEND);
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"
- تم انشاء بوت مكتبة السادس خاص بك
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- اضغط هنا للدخول الى البوت",'url'=>"https://t.me/$userr"]],],])]);
}
if($data == 'Back'){
bot('editMessageText',['chat_id'=>$chat_id2,'message_id'=>$message_id,'text'=>"- اهلا بك عزيزي في بوت مصنع بوتات التليكرام
- اضغط على اصنع بوت واصنع البوت الخاص بك الان مجانا!
",'parse_mode'=>"markdown",'disable_web_page_preview'=>true,'reply_markup'=>json_encode(['inline_keyboard'=>[[['text'=>'- اصنع بوت','callback_data'=>'makebot']],],])]);}
$BROKDOWN = count($done_down)-1;
$BROKHMS = count($done_hms)-1;
$BROKSAYT = count($done_sayt)-1;
$BROKTWSL = count($done_twsl)-1;
$BROKZKRF = count($done_zkrf)-1;
$BROKBUY = count($done_buy)-1;
$BROKCONVERT = count($done_convert)-1;
$BROKFLAN = count($done_flan)-1;
$BROKKHERA = count($done_khera)-1;
$BROKMARKDOWN = count($done_markdown)-1;
$BROKSIXTH = count($done_sixth)-1;
$BROKSAFECH = count($dond_safech)-1;
$BROKALL = $BROKDOWN + $BROKHMS + $BROKSAYT + $BROKTWSL + $BROKZKRF + $BROKBUY + $BROKCONVERT + $BROKSAFECH + $BROKMARKDOWN + $BROKSIXTH + $BROKKHERA + $BROKFLAN;
if($data == 'status'){
bot('editMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
- عدد بوتات التحميل من الفيس + الانستا المصنوعه => $BROKDOWN
- عدد بوتات الهمسه المصنوعه => $BROKHMS
- عدد بوتات السايت المصنوعه => $BROKSAYT
- عدد بوتات التواصل المصنوعه => $BROKTWSL
- عدد بوتات الزخرفه المصنوعه => $BROKZKRF
- عدد بوتات المتجر المصنوعه => $BROKBUY
- عدد بوتات تحويل الصيغ المصنوعه => $BROKCONVERT
- عدد بوتات شنو رأيك بفلان المصنوعه => $BROKFLAN
- عدد بوتات الخيره المصنوعه => $BROKKHERA
- عدد بوتات صنع الازرار الشفافه المصنوعه => $BROKMARKDOWN
- عدد بوتات حماية القنوات المصنوعه => $BROKSAFECH
- عدد بوتات مكتبة السادس المصنوعه => $BROKSIXTH
- - - - - - -
- عدد جميع البوتات المصنوعه => $BROKALL
- عدد اعضاء البوت => $x_BRK3
",
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'- رجوع' ,'callback_data'=>"x_BRK"]],
]])
]);
} 
