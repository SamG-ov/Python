<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #6aab73;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">data </span><span class="s0">import </span><span class="s1">question_data</span>
<span class="s0">from </span><span class="s1">question_model </span><span class="s0">import </span><span class="s1">Question</span>
<span class="s0">from </span><span class="s1">quiz_brain </span><span class="s0">import </span><span class="s1">QuizBrain</span>

<span class="s1">question_bank </span><span class="s2">= []</span>
<span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">question_data</span><span class="s2">:</span>
    <span class="s1">question_text </span><span class="s2">= </span><span class="s1">i</span><span class="s2">[</span><span class="s3">&quot;text&quot;</span><span class="s2">]</span>
    <span class="s1">question_answer </span><span class="s2">= </span><span class="s1">i</span><span class="s2">[</span><span class="s3">&quot;answer&quot;</span><span class="s2">]</span>
    <span class="s1">new_question </span><span class="s2">= </span><span class="s1">Question</span><span class="s2">(</span><span class="s1">question_text</span><span class="s2">, </span><span class="s1">question_answer</span><span class="s2">)</span>
    <span class="s1">question_bank</span><span class="s2">.</span><span class="s1">append</span><span class="s2">(</span><span class="s1">new_question</span><span class="s2">)</span>

<span class="s1">quiz </span><span class="s2">= </span><span class="s1">QuizBrain</span><span class="s2">(</span><span class="s1">question_bank</span><span class="s2">)</span>
<span class="s0">while </span><span class="s1">quiz</span><span class="s2">.</span><span class="s1">stillHasQuestions</span><span class="s2">():</span>
    <span class="s1">quiz</span><span class="s2">.</span><span class="s1">nextQuestion</span><span class="s2">()</span>

<span class="s1">print</span><span class="s2">(</span><span class="s3">&quot;The game is over&quot;</span><span class="s2">)</span>
<span class="s1">print</span><span class="s2">(</span><span class="s3">f&quot;Your score is: </span><span class="s0">{</span><span class="s1">quiz</span><span class="s2">.</span><span class="s1">score</span><span class="s0">}</span><span class="s3">&quot;</span><span class="s2">)</span>
</pre>
</body>
</html>