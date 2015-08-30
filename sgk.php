<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>天网查询系统</title>
<style>
.main{
	margin:0px auto;
	padding:0px;
	width:1536px;
	background:#f3f3f3;
	border:1px #ccc solid;
	font-size:12px;
}
.center{
	margin-top:30px;
	text-align:center;
}
.result{
	margin-top:30px;
	text-align:center;
	margin-bottom:30px;
	line-height: 20px;
	font-size: 14px;
}
.key{
	height:28px;
	width:400px;
	padding:0px;
	margin:0px;
	font-size:14px;
	line-height:28px;
	border:1px #333 solid;
}
.stype{
	padding:0px;
	margin:0px;
	height:25px;
	border:1px #333 solid;
	}
.table{
border-collapse: collapse;
background:#fff;
color:#464646;
}
.td{
	border: 1px #ccc solid;
}
</style>
</head>
<!--
社工库为两个表
QQ群信息一个，数据库名为qun，表前缀分别为:shegong_qun_qunlist和shegong_qun_group
其他数据为另一个数据库，名为shegong，表前缀为：shegong_
-->
<body>
<div class="main">
    <div class="center">
    	<a href='index.php'><h1></>天网查询系统</h1></></a>
    <form action="index.php" method="GET" enctype="application/x-www-form-urlencoded" name="query">
    <select name="op" class="stype">
			<option value="email">邮	箱</option>
			<option value="name">用户名</option>
			<option value="realname">姓	名</option>
			<option value="tel">手	机</option>
			<option value="ip">IP</option>
			<option value="ctfid">身份证</option>
			<option value="passwd">密码</option>
			<option value="domain">域名</option>
			<option value="QQNum">Q	Q</option>
			<option value="Qun">QQ for 群</option>
			<option value="QunNum">Q群	for QQ</option>
			<option value="QunName">姓名 for QQ群</option>
		</select>
	<input name="key" class="key" id="keyy" value="共计数据2716723428条" onmouseout="this.style.borderColor=''" onFocus="if (value =='共计数据2716723428条'){value =''}" onBlur="if (value ==''){value='共计数据2716723428条'}"/> 
             &nbsp;&nbsp;模糊寻找 <input name="liketype" type="checkbox" value="1" align="absmiddle" class="ck"/>&nbsp;&nbsp;
        <input name="" type="submit" value="查询" height="30" width="80"/>
    </form>
    </div>
    <div class="result">
<?php
$key		=	post_check($_GET['key']);
$op			=	post_check($_GET['op']);
$liketype	=	post_check($_GET['liketype']);
/* 防注入函数 */
function post_check($post) {  
  if (!get_magic_quotes_gpc()) { 
    $post = addslashes($post);
  }  
  $post = str_replace("_", "\_", $post);
  $post = str_replace("%", "\%", $post);
  $post = nl2br($post);
  $post = htmlspecialchars($post);
  return $post;  
}  
/* 连接选择数据库 */
$link = mysql_connect("localhost", "root", "")
   or die("Could not connect : " . mysql_error()); 
mysql_select_db("shegong") or die("Could not select database");
mysql_query("SET NAMES 'UTF8'"); 
/* 执行 SQL 查询 */
/* 在 HTML 中打印结果 */
/*QQ群内容查询*/
if($op =='Qun'){
	$t1 = microtime(true);
	print "<table border=\"1\"> <caption> <h3>QQ群关系</caption>";
	print "<td><b1>QQ号码</b1></td><td><b1>QQ昵称</b1></td><td><b1>QQ群号</b1></td><td><b1>QQ群标题</b1></td><td><b1>QQ群内容</b1></td></tr>";
	$query = "select table_name from information_schema.tables Where table_name LIKE 'shegong_qun_group%'";
	$result = mysql_query($query) or die("Query failed : " . mysql_error()); 
	while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
		foreach ($line as $col_value) {
			$sql_plus = "select QQNum,Nick,QunNum from qun.$col_value where QQNum = '$key';";
			$values = mysql_query($sql_plus); 
			while ($task = mysql_fetch_array($values, MYSQL_ASSOC)) {
				foreach($task as $value){
					echo "<td><b1>$value</b1></td>";
				}
				$query_quninfo = "select table_name from information_schema.tables Where table_name LIKE 'shegong_qun_qunlist%'";
				$result_quninfo = mysql_query($query_quninfo) or die("Query failed : " . mysql_error()); 
				while ($line_quninfo = mysql_fetch_array($result_quninfo, MYSQL_ASSOC)) {
					foreach ($line_quninfo as $quninfo_value) {
						$sql_plus_quninfo = "select Title,QunText from qun.$quninfo_value where QunNum = $task[QunNum];";
						$values_quninfo = mysql_query($sql_plus_quninfo); 
						while ($task_quninfo = mysql_fetch_array($values_quninfo, MYSQL_ASSOC)) {
							foreach($task_quninfo as $value_quninfo){
								print "<td><b1>$value_quninfo</b1></td>";
							}
						}
					}
				}
				echo "</tr>";
			}
		}
	}
	$t2 = microtime(true);
	print "</table>";
	print "<h2><span style=\"color:red\">耗时".round($t2-$t1,3)."秒</span></h2>";
	print "</div></body></html>";
}

if($op =='QunNum'){
	$t1 = microtime(true);
	print "<table border=\"1\"> <caption> <h3>QQ群关系</caption>";
	print "<td><b1>QQ号码</b1></td><td><b1>QQ昵称</b1></td><td><b1>QQ群号</b1></td><td><b1>QQ群标题</b1></td><td><b1>QQ群内容</b1></td></tr>";
	$query = "select table_name from information_schema.tables Where table_name LIKE 'shegong_qun_group%'";
	$result = mysql_query($query) or die("Query failed : " . mysql_error()); 
	while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
		foreach ($line as $col_value) {
			$sql_plus = "select QQNum,Nick,QunNum from qun.$col_value where QunNum = '$key';";
			$values = mysql_query($sql_plus); 
			while ($task = mysql_fetch_array($values, MYSQL_ASSOC)) {
				foreach($task as $value){
					echo "<td><b1>$value</b1></td>";
				}
				$query_quninfo = "select table_name from information_schema.tables Where table_name LIKE 'shegong_qun_qunlist%'";
				$result_quninfo = mysql_query($query_quninfo) or die("Query failed : " . mysql_error()); 
				while ($line_quninfo = mysql_fetch_array($result_quninfo, MYSQL_ASSOC)) {
					foreach ($line_quninfo as $quninfo_value) {
						$sql_plus_quninfo = "select Title,QunText from qun.$quninfo_value where QunNum = $task[QunNum];";
						$values_quninfo = mysql_query($sql_plus_quninfo); 
						while ($task_quninfo = mysql_fetch_array($values_quninfo, MYSQL_ASSOC)) {
							foreach($task_quninfo as $value_quninfo){
								print "<td><b1>$value_quninfo</b1></td>";
							}
						}
					}
				}
				echo "</tr>";
			}
		}
	}
	$t2 = microtime(true);
	print "</table>";
	print "<h2><span style=\"color:red\">耗时".round($t2-$t1,3)."秒</span></h2>";
	print "</div></body></html>";
}

if($op =='QunName'){
	$t1 = microtime(true);
	print "<table border=\"1\"> <caption> <h3>QQ群关系</caption>";
	print "<td><b1>姓名</b1></td><td><b1>年龄</b1></td><td><b1>性别</b1></td><td><b1>QQ</b1></td><td><b1>QQ群</b1></td><td><b1>QQ群标题</b1></td><td><b1>QQ群内容</b1></td><tr>";
	$query = "select table_name from information_schema.tables Where table_name LIKE 'shegong_qun_group%'";
	$result = mysql_query($query) or die("Query failed : " . mysql_error()); 
	while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
		foreach ($line as $col_value) {
			$sql_plus = "select realname,Age,Gender,QQNum,QunNum from qun.$col_value where realname = '$key';";
			$values = mysql_query($sql_plus); 
			while ($task = mysql_fetch_array($values, MYSQL_ASSOC)) {
				foreach($task as $value){
					echo "<td><b1>$value</b1></td>";
				}
				$query_quninfo = "select table_name from information_schema.tables Where table_name LIKE 'shegong_qun_qunlist%'";
				$result_quninfo = mysql_query($query_quninfo) or die("Query failed : " . mysql_error()); 
				while ($line_quninfo = mysql_fetch_array($result_quninfo, MYSQL_ASSOC)) {
					foreach ($line_quninfo as $quninfo_value) {
						$sql_plus_quninfo = "select Title,QunText from qun.$quninfo_value where QunNum = $task[QunNum];";
						$values_quninfo = mysql_query($sql_plus_quninfo); 
						while ($task_quninfo = mysql_fetch_array($values_quninfo, MYSQL_ASSOC)) {
							foreach($task_quninfo as $value_quninfo){
								print "<td><b1>$value_quninfo</b1></td>";
							}
						}
					}
				}
				echo "</tr>";
			}
		}
	}



	$t2 = microtime(true);
	print "</table>";
	print "<h2><span style=\"color:red\">耗时".round($t2-$t1,3)."秒</span></h2>";
	print "</div></body></html>";
}

if($op =='email' || $op == 'name' || $op == 'realname' || $op =='tel' || $op == 'QQNum' || $op == 'ctfid' || $op == 'ip' || $op == 'passwd' || $op == 'domain'){
	$t1 = microtime(true);
	$query = "select table_name from information_schema.tables Where table_name LIKE 'shegong_%'";
	$result = mysql_query($query) or die("Query failed : " . mysql_error()); 
	while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
		foreach ($line as $col_value) {
			if(empty($liketype)){
				$sql_plus = "select * from $col_value where $op = '$key';";
			}
			else{
				$sql_plus = "select * from $col_value where $op like '%$key%';";
			}
			$values = mysql_query($sql_plus); 
			while ($task = mysql_fetch_array($values, MYSQL_ASSOC)) {
				$show_table = "select COLUMN_NAME from information_schema.COLUMNS where table_name ='$col_value'";
				$tables = mysql_query($show_table);
				print "<table border=\"1\"> <caption> <h3>From : <strong> $col_value</strong> </h3> </caption>";
				while ($table = mysql_fetch_array($tables, MYSQL_ASSOC)){
					foreach ($table as $t){
						print "<td><b1>$t</b1></td>";}}
					print "</tr>";
					foreach ($task as $make) {
						print "<td>$make</td>";
					}
					print "</table><br><br>";
				}
		}
	}
	$t2 = microtime(true);
	print "</table>";
	print "<h2><span style=\"color:red\">耗时".round($t2-$t1,3)."秒</span></h2>";
	print "</div></body></html>";
}
?>

