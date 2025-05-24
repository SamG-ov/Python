<html>
<head>
<title>quiz_brain.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #2aacb8;}
.s4 { color: #6aab73;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
quiz_brain.py</font>
</center></td></tr></table>
<pre><span class="s0">class </span><span class="s1">QuizBrain</span><span class="s2">:</span>

    <span class="s0">def </span><span class="s1">__init__</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">list</span><span class="s2">):</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">question_number </span><span class="s2">= </span><span class="s3">0</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">list </span><span class="s2">= </span><span class="s1">list</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">score </span><span class="s2">= </span><span class="s3">0</span>

    <span class="s0">def </span><span class="s1">stillHasQuestions</span><span class="s2">(</span><span class="s1">self</span><span class="s2">):</span>
        <span class="s0">return </span><span class="s1">self</span><span class="s2">.</span><span class="s1">question_number </span><span class="s2">&lt; </span><span class="s1">len</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">list</span><span class="s2">)</span>

    <span class="s0">def </span><span class="s1">nextQuestion</span><span class="s2">(</span><span class="s1">self</span><span class="s2">):</span>
        <span class="s1">currentQuestion </span><span class="s2">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">list</span><span class="s2">[</span><span class="s1">self</span><span class="s2">.</span><span class="s1">question_number</span><span class="s2">]</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">question_number </span><span class="s2">+= </span><span class="s3">1</span>
        <span class="s1">userAnswer </span><span class="s2">= </span><span class="s1">input</span><span class="s2">(</span><span class="s4">f&quot;Q.</span><span class="s0">{</span><span class="s1">self</span><span class="s2">.</span><span class="s1">question_number</span><span class="s0">}</span><span class="s4">: </span><span class="s0">{</span><span class="s1">currentQuestion</span><span class="s2">.</span><span class="s1">question</span><span class="s0">} </span><span class="s4">(True or False): &quot;</span><span class="s2">)</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">checkAnswer</span><span class="s2">(</span><span class="s1">userAnswer</span><span class="s2">, </span><span class="s1">currentQuestion</span><span class="s2">.</span><span class="s1">answer</span><span class="s2">)</span>

    <span class="s0">def </span><span class="s1">checkAnswer</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">userAnswer</span><span class="s2">, </span><span class="s1">correctAnswer</span><span class="s2">):</span>
        <span class="s0">if </span><span class="s1">userAnswer </span><span class="s2">== </span><span class="s1">correctAnswer</span><span class="s2">:</span>
            <span class="s1">print</span><span class="s2">(</span><span class="s4">&quot;Correct!!!&quot;</span><span class="s2">)</span>
            <span class="s1">self</span><span class="s2">.</span><span class="s1">score </span><span class="s2">+= </span><span class="s3">1</span>
        <span class="s0">else</span><span class="s2">:</span>
            <span class="s1">print</span><span class="s2">(</span><span class="s4">f&quot;Wrong!!! Correct answer was </span><span class="s0">{</span><span class="s1">correctAnswer</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s2">)</span>
        <span class="s1">print</span><span class="s2">(</span><span class="s4">f&quot;Your current score is </span><span class="s0">{</span><span class="s1">self</span><span class="s2">.</span><span class="s1">score</span><span class="s0">}</span><span class="s4">/</span><span class="s0">{</span><span class="s1">self</span><span class="s2">.</span><span class="s1">question_number</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s2">)</span></pre>
</body>
</html>