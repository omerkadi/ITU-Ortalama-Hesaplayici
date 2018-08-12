site_data = """
<html lang="en" class="gr__ssb_sis_itu_edu_tr"><head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="Pragma" name="Cache-Control" content="no-cache">
<meta http-equiv="Cache-Control" name="Cache-Control" content="no-cache">
<link rel="stylesheet" href="/css/web_defaultapp.css" type="text/css">
<link rel="stylesheet" href="/css/web_defaultprint.css" type="text/css" media="print">
<meta http-equiv="Content-Script-Type" name="Default_Script_Language" content="text/javascript">
<script language="JavaScript" type="text/javascript">
<!-- Hide JavaScript from older browsers 
var submitcount=0;
function checkSubmit() {
if (submitcount == 0)
   {
   submitcount++;
   return true;
   }
else
   {
alert("Your changes have already been submitted.");
   return false;
   }
}
//  End script hiding -->
</script>
<script language="JavaScript" type="text/javascript">
<!-- Hide JavaScript from older browsers 
//  Function to open a window
function windowOpen(window_url) {
   helpWin = window.open(window_url,'','toolbar=yes,status=no,scrollbars=yes,menubar=yes,resizable=yes,directories=no,location=no,width=350,height=400');
   if (document.images) { 
       if (helpWin) helpWin.focus()
   }
}
//  End script hiding -->
</script>
<style type="text/css">/*.lleo_errorSelection *::-moz-selection,
.lleo_errorSelection *::selection,
.lleo_errorSelection *::-webkit-selection {
    background-color: red !important;
    color: #fff !important;;
}*/

#lleo_dialog,
#lleo_dialog * {
    color: #000 !important;
    font: normal 13px Arial, Helvetica !important;
    line-height: 15px !important;
    margin: 0 !important;
	padding: 0 !important;
	background: none !important;
	border: none 0 !important;
	position: static !important;
	vertical-align: baseline !important;
	overflow: visible !important;
	width: auto !important;
	height: auto !important;
    max-width: none !important;
    max-height: none !important;
	float: none !important;
	visibility: visible !important;
	text-align: left !important;
    text-transform: none !important;
	border-collapse: separate !important;
	border-spacing: 2px !important;
    box-sizing: content-box !important;
    box-shadow: none !important;
    opacity: 1 !important;
    text-shadow: none !important;
    letter-spacing: normal !important;
    -webkit-filter: none !important;
    -moz-filter: none !important;
    filter: none !important;
}
#lleo_dialog *:before,
#lleo_dialog *:after {
    content: '';
}

#lleo_dialog iframe {
	height: 0 !important;
	width: 0 !important;
}

#lleo_dialog {
    position: absolute !important;
    background: #fff !important;
    border: solid 1px #ccc !important;
    padding: 7px 0 0 !important;
    left: -999px;
    top: -999px;
    width: 440px !important;
    overflow: hidden;
    display: block !important;
    z-index: 999999999 !important;
    box-shadow: 8px 16px 30px rgba(0, 0, 0, 0.16) !important;
    border-radius: 3px !important;
    opacity: 0 !important;
    -webkit-transform: translateY(15px);
    -moz-transform: translateY(15px);
    -ms-transform: translateY(15px);
    -o-transform: translateY(15px);
    transform: translateY(15px);
}
#lleo_dialog.lleo_show_small {
    width: 150px !important;
}
#lleo_dialog.lleo_show {
    opacity: 1 !important;
    -webkit-transform: translateY(0);
    -moz-transform: translateY(0);
    -ms-transform: translateY(0);
    -o-transform: translateY(0);
    transform: translateY(0);
    -webkit-transition: -webkit-transform 0.3s, opacity 0.3s !important;
    -moz-transition: -moz-transform 0.3s, opacity 0.3s !important;
    -ms-transition: -ms-transform 0.3s, opacity 0.3s !important;
    -o-transition: -o-transform 0.3s, opacity 0.3s !important;
    transition: transform 0.3s, opacity 0.3s !important;
}
#lleo_dialog.lleo_collapse {
    opacity: 0 !important;
    -webkit-transform: scale(0.25, 0.1) translate(-550px, 100px);
    -moz-transform: scale(0.25, 0.1) translate(-550px, 100px);
    -ms-transform: scale(0.25, 0.1) translate(-550px, 100px);
    -o-transform: scale(0.25, 0.1) translate(-550px, 100px);
    transform: scale(0.25, 0.1) translate(-550px, 100px);
    -webkit-transition: -webkit-transform 0.4s, opacity 0.4s !important;
    -moz-transition: -moz-transform 0.4s, opacity 0.4s !important;
    -ms-transition: -ms-transform 0.4s, opacity 0.4s !important;
    -o-transition: -o-transform 0.4s, opacity 0.4s !important;
    transition: transform 0.4s, opacity 0.4s !important;
}
#lleo_dialog input::-webkit-input-placeholder {
    color: #aaa !important;
}
#lleo_dialog .lleo_has_pic #lleo_word {
	margin-right: 80px !important;
}
#lleo_dialog #lleo_translationsContainer1 {
	position: relative !important;
}
#lleo_dialog #lleo_translationsContainer2 {
	padding: 7px 0 0 !important;
	vertical-align: middle !important;
}
#lleo_dialog #lleo_word {
    color: #000 !important;
    margin: 0 5px 2px 0 !important;
    /*float: left !important;*/
}
#lleo_dialog .lleo_has_sound #lleo_word {
    margin-left: 30px !important;
}
#lleo_dialog #lleo_text {
    font-weight: bold !important;
    color: #d56e00 !important;
    text-decoration: none !important;
    cursor: default !important;
}
/*
#lleo_dialog #lleo_text.lleo_known {
    cursor: pointer !important;
    text-decoration: underline !important;
}
*/
/*#lleo_dialog #lleo_closeBtn {
    position: absolute !important;
    right: 6px !important;
    top: 5px !important;
    line-height: 1px !important;
    text-decoration: none !important;
    font-weight: bold !important;
    font-size: 0 !important;
    color: #aaa !important;
    display: block !important;
	z-index: 9999999999 !important;
	width: 7px !important;
	height: 7px !important;
	padding: 0 !important;
	margin: 0 !important;
}*/

#lleo_dialog #lleo_optionsBtn {
    position: absolute !important; 
    right: 3px !important;
    top: 5px !important;
    line-height: 1px !important;
    text-decoration: none !important;
    font-weight: bold !important;
    font-size: 13px !important;
    color: #aaa !important;
    padding: 2px !important;
	display: none;
}
    #lleo_dialog.lleo_optionsShown #lleo_optionsBtn {
        display: block !important;
    }
    #lleo_dialog #lleo_optionsBtn img {
        width: 12px !important;
        height: 12px !important;
    }
#lleo_dialog #lleo_sound {
    float: left !important;
    width: 16px !important;
    height: 16px !important;
    margin-left: 9px !important;
    margin-right: 3px !important;
    background: 0 0 no-repeat !important;
    cursor: pointer !important;
    display: none !important;
    background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAfNJREFUeNq0U01IVFEU/u57Oo5WhBRIBBptykWLYBa2soWiEKQQEbrSFsGbVRQKQc2iFqGitXqvjQxCoCJCqyI0aBUtZILaJNUuYWYWo8HovJ/707nP94bnz0rxwvfOuefd8517fi5TSuE4i50YwZ3l37ZhNlpgzFkaaM/G9sHF1YskNrT+7l4PjMOcb78t2JL71uxgB+2UlfxHTtq5N94fIOh/88kWgWfl73ZCSQkpeGg3H091JY6dI2S00qA/N3KO3dDUYhFgEmZGurG+w9FqApIHsVM7kaTF9Nhn0r8Q7hPWQgIRuNaH3AMUA4W/Lkdh04cpFS43G0TgxQTvCdMETVAk3KynIHwXZU/ge8XDt7KH9bKLjU0P2zVO5LsEpSejVRJ9UR18EtfqKegovs9R3Q6w9c/H1o4Aa2Jwm1lIvn9RJ4w9RdRRzqcYrpwycCll4Cy1lnkS3Bc6vfBg28v8aRIfI78zhB/1GygROH3jLyyzMQ0zlUZuZBSlKkeLoegGtTjYLcJ8pF+NakHOFC2J6w+f25mxSfWrWFF/ShXVPTGvtN14NNkVnxlYWJkgZEL7/vwKr55lKSVnaGYWkuYgrgG172uUv47+U7fw0EHaJXmalUQy/HqO6lBzEsVjJC4Q8kd6TETQpjuaGOvjv8b/AgwA/ij1XMx58NIAAAAASUVORK5CYII=) !important;
}
#lleo_dialog .lleo_has_sound #lleo_sound {
    display: block !important;
}

#lleo_dialog #lleo_soundWave {
    border: solid 5px #4495CC !important;
    border-radius: 5px !important;
    position: absolute !important;
    left: -5px !important;
    top: -5px !important;
    right: -5px !important;
    bottom: -5px !important;
    z-index: 0 !important;
    opacity: 0.9 !important;
    display: none !important;
}
    #lleo_dialog #lleo_soundWave.lleo_beforePlaying {
        display: block !important;
    }
    #lleo_dialog #lleo_soundWave.lleo_playing {
        opacity: 0 !important;
        border-width: 20px !important;
        border-radius: 30px !important;

        -webkit-transform: scale(1.07,1.1) !important;
        -moz-transform: scale(1.07,1.1) !important;
        -ms-transform: scale(1.07,1.1) !important;
        transform: scale(1.07,1.1) !important;

        -webkit-transition: all 0.6s !important;
        -moz-transition: all 0.6s !important;
        -ms-transition: all 0.6s !important;
        transition: all 0.6s !important;
    }


#lleo_dialog #lleo_picOuter {
    position: absolute !important;
    float: right !important;
    top: 4px;
    right: 5px;
    z-index: 9 !important;
    display: none !important;
    width: 100px !important;
}
    #lleo_dialog.lleo_optionsShown #lleo_picOuter {
        right: 25px;
    }
#lleo_dialog .lleo_has_pic #lleo_picOuter {
    display: block !important;
}
    #lleo_dialog #lleo_picOuter:hover {
        width: auto !important;
        z-index: 11 !important;
    }
#lleo_dialog #lleo_pic,
#lleo_dialog #lleo_picBig {
    position: absolute !important;
    top: 0 !important;
    right: 0 !important;
    border: solid 2px #fff !important;
    -webkit-border-radius: 2px !important;
    -moz-border-radius: 2px !important;
	border-radius: 2px !important;
    z-index: 1 !important;
}
#lleo_dialog #lleo_pic {
	position: relative !important;
    border: none !important;
	width: 30px !important;
}
#lleo_dialog #lleo_picBig {
    box-shadow: -1px 2px 4px rgba(0,0,0,0.3);
    z-index: 2 !important;
    opacity: 0 !important;
    visibility: hidden !important;
}
    #lleo_dialog #lleo_picOuter:hover #lleo_picBig {
        visibility: visible !important;
        opacity: 1 !important;
        -webkit-transition: opacity 0.3s !important;
        -webkit-transition-delay: 0.3s !important;
    }
#lleo_dialog #lleo_transcription {
    margin: 0 80px 4px 31px !important;
    color: #aaaaaa !important;
}
#lleo_dialog .lleo_no_trans {
    color: #aaa !important;
}

#lleo_dialog .ll-translation-counter {
	float: right !important;
    font-size: 11px !important;
    color: #aaa !important;
    padding: 2px 2px 1px 10px !important;
}

#lleo_dialog .ll-translation-text {
	float: left !important;
	/*width: 80% !important;*/
}

#lleo_dialog #lleo_trans a {
    color: #3F669F !important;
    text-decoration: none !important;
    text-overflow: ellipsis !important;
    padding: 1px 4px !important;
    overflow: hidden !important;
    float: left !important;
    width: 320px !important;
}

#lleo_dialog .ll-translation-item {
    color: #3F669F !important;
    border: solid 1px #fff !important;
    padding: 3px !important;
    width: 100% !important;
    float: left !important;
	-moz-border-radius: 2px !important;
	-webkit-border-radius: 2px !important;
	border-radius: 2px !important;
}

#lleo_dialog .ll-translation-item:hover {
	border: solid 1px #9FC2C9 !important;
    background: #EDF4F6 !important;
	cursor: pointer !important;
}
#lleo_dialog .ll-translation-item:hover .ll-translation-counter {
	color: #83a0a6 !important;
}

#lleo_dialog .ll-translation-marker {
    background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAWSURBVBhXY7RPm/+fAQkwIXNAbMICAJQ8AkvqWg/SAAAAAElFTkSuQmCC) !important;
    display: inline-block !important;
    width: 4px !important;
    height: 4px !important;
    margin: 7px 5px 2px 2px !important;
    float: left !important;
}

#lleo_dialog #lleo_icons {
    color: #aaa !important;
    font-size: 11px !important;
    background: #f8f8f8 !important;
    padding: 10px 10px 10px 16px !important;
}
#lleo_icons a {
    display: inline-block !important;
    width: 16px !important;
    height: 16px !important;
    margin: 0 10px -4px 3px !important;
    text-decoration: none !important;
    opacity: 0.5 !important;
    background: url(data:image/png;base64,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) !important;
}
#lleo_icons a:hover {
    opacity: 1 !important;
}
#lleo_icons a.lleo_google     {background-position:-34px 0 !important;}
#lleo_icons a.lleo_multitran  {background-position:-64px 0 !important;}
#lleo_icons a.lleo_lingvo     {background-position:-51px 0 !important; width: 12px !important;}
#lleo_icons a.lleo_dict       {background-position:-17px 0 !important;}
#lleo_icons a.lleo_linguee    {background-position:-81px 0 !important;}
#lleo_icons a.lleo_michaelis  {background-position:-98px 0 !important;}

#lleo_dialog #lleo_contextContainer {
    margin: 0 !important;
    padding: 3px 15px 8px 10px !important;
    background: #eee !important;
    background: -webkit-gradient(linear, left top, left bottom, from(#fff), to(#eee)) !important;
    background: -moz-linear-gradient(-90deg, #fff, #eee) !important;
    border-bottom: solid 1px #ddd !important;
    border-top-left-radius: 3px !important;
    border-top-right-radius: 3px !important;
    display: none !important;
    overflow: hidden !important;
}
#lleo_dialog .lleo_has_context #lleo_contextContainer {
    display: block !important;
}
#lleo_dialog #lleo_context {
    color: #444 !important;
    text-shadow: 1px 1px 0 #f4f4f4 !important;
    line-height: 12px !important;
    font-size: 11px !important;
    margin-left: 2px !important;
}
#lleo_dialog #lleo_context b {
    line-height: 12px !important;
    color: #000 !important;
    font-weight: bold !important;
    font-size: 11px !important;
}
/*#lleo_dialog #lleo_gBrand {
    color: #aaa !important;
    font-size: 10px !important;
    *//*padding-right: 52px !important;*//*
    padding-bottom: 14px !important;
    margin: -3px 4px 0 4px !important;
    background: left bottom url(data:image/png;base64,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) no-repeat !important;
    display: inline-block !important;
    float: right !important;
}
#lleo_dialog #lleo_gBrand.hidden {
    display: none !important;
}*/
#lleo_dialog #lleo_translateContextLink {
    color: #444 !important;
    text-shadow: 1px 1px 0 #f4f4f4 !important;
    background: -webkit-gradient(linear, left top, left bottom, from(#f4f4f4), to(#ddd)) !important;
    background: -moz-linear-gradient(-90deg, #f4f4f4, #ddd) !important;
    border: solid 1px !important;
    box-shadow: 1px 1px 0 #f6f6f6 !important;
    border-color: #999 #aaa #aaa #999 !important;
    -moz-border-radius: 2px !important;
	-webkit-border-radius: 2px !important;
	border-radius: 2px !important;
    padding: 0 3px !important;
    font-size: 11px !important;
    text-decoration: none !important;
    margin: 1px 5px 0 !important;
    display: inline-block !important;
    white-space: nowrap !important;
}
#lleo_dialog #lleo_translateContextLink:hover {
    background: #f8f8f8 !important;
}
#lleo_dialog #lleo_translateContextLink.hidden {
    visibility: hidden !important;
}

#lleo_dialog #lleo_setTransForm {
    display: block !important;
    margin-top: 3px !important;
    padding-top: 5px !important;
    /* Set position and background because the form might be overlapped by an image when no translations */
    position: relative !important;
    background: #fff !important;
    z-index: 10 !important;
    padding-bottom: 10px !important;
    padding-left: 16px !important;
}
#lleo_dialog .lleo-custom-translation {
    padding: 4px 5px !important;
    border: solid 1px #ddd !important;
	border-radius: 2px !important;
    width: 90% !important;
    min-width: 270px !important;
    background: -webkit-gradient(linear, 0 0, 0 20, from(#f1f1f1), to(#fff)) !important;
    background: -moz-linear-gradient(-90deg, #f1f1f1, #fff) !important;
	font: normal 13px Arial, Helvetica !important;
	line-height: 15px !important;
}
#lleo_dialog .lleo-custom-translation:hover {
    border: solid 1px #aaa !important;
}
#lleo_dialog .lleo-custom-translation:focus {
    background: #FFFEC9 !important;
}

#lleo_dialog *.hidden {
    display: none !important;
}

#lleo_dialog .infinitive{
    color: #D56E00 !important;
    text-decoration: none;
    border-bottom: 1px dotted #D56E00 !important;
}
#lleo_dialog .infinitive:hover{
    border: none !important;
}

#lleo_dialog .lleo_separator {
    height: 1px !important;
    background: #eee;
    margin-top: 10px !important;
    background: -webkit-linear-gradient(left, rgba(255,255,255,1) 0%,#eee 8%,rgba(255,255,255,1) 80%) !important;
    background: -moz-linear-gradient(left, rgba(255,255,255,1) 0%, #eee 8%, rgba(255,255,255,1) 80%) !important;
    background: -ms-linear-gradient(left, rgba(255,255,255,1) 0%,#eee 8%,rgba(255,255,255,1) 80%) !important;
    background: linear-gradient(to right, rgba(255,255,255,1) 0%,#eee 8%,rgba(255,255,255,1) 80%) !important;
}
#lleo_dialog #lleo_trans {
    /*border-top: 1px solid #eeeeee !important;*/
    padding: 5px 30px 0 14px !important;
    zoom: 1;
}

#lleo_dialog .lleo_clearfix {
	display: block !important;
	clear: both !important;
	visibility: hidden !important;
	height: 0 !important;
	font-size: 0 !important;
}


#lleo_dialog #lleo_picOuter table {
    width: 44px !important;
    position: absolute !important;
    right: 0 !important;
    top: 0 !important;
    vertical-align: middle !important;
}

#lleo_dialog #lleo_picOuter td {
    width: 38px !important;
    height: 38px !important;
    /*border: 1px solid #eeeeee !important;*/
    vertical-align: middle !important;
    text-align: center !important;
}

#lleo_dialog #lleo_picOuter td div {
	height: 38px !important;
	overflow: hidden !important;
}

#lleo_dialog .lleo_empty {
    margin: 0 5px 7px !important;
}

#lleo_youtubeExportBtn {
    margin-left: 10px;
    height: 24px;
}
    #lleo_youtubeExportBtn i {
        display: inline-block;
        width: 16px;
        height: 16px;
        background: 0 0 url(https://d144fqpiyasmrr.cloudfront.net/plugins/all/images/i16.png) !important;
    }
    #lleo_youtubeExportBtn .yt-uix-button-content {
        font-size: 12px;
        line-height: 2px;
    }


/*** Parsed Lyrics Content *****************************/

.lleo_lyrics tran {
    background: transparent !important;
    border-radius: 2px !important;
    text-shadow: none !important;
    cursor: pointer !important;
}
    .lleo_lyrics tran:hover {
        color: #fff !important;
        background: #C77213 !important;
        -webkit-transition: all 0.1s !important;
        -moz-transition: all 0.1s !important;
        -ms-transition: all 0.1s !important;
        -o-transition: all 0.1s !important;
        transition: all 0.1s !important;
    }

.lleo_songName {
    border: solid 1px #ffd47c;
    background: #fff1c2;
    border-radius: 2px;
}

.lleo_hidden_iframe {
    visibility: hidden;
}</style></head>
<body style=" font-size: 12pt; font-family: Arial" data-gr-c-s-loaded="true">
<div class="headerwrapperdiv">
<div class="pageheaderdiv1">
<a href="#main_content" onmouseover="window.status='Go to Main Content'; return true" onmouseout="window.status=''; return true" onfocus="window.status='Go to Main Content'; return true" onblur="window.status=''; return true" class="skiplinks">Go to Main Content</a>
<h1>Istanbul Teknik Universitesi</h1></div><div class="headerlinksdiv">
<span class="pageheaderlinks2">
<map name="Module_Navigation_Links_H" title="Module Navigation Links">
<p>
<a href="#skip_Module_Navigation_Links_H" onmouseover="window.status='Skip Module Navigation Links'; return true" onmouseout="window.status=''; return true" onfocus="window.status='Skip Module Navigation Links'; return true" onblur="window.status=''; return true" class="skiplinks">Skip Module Navigation Links</a>
</p><table class="plaintable" summary="This is main table for displaying Tab Items." width="100%" cellspacing="0" cellpadding="0" border="0">
<tbody><tr>
<td class="pldefault">
<table class="plaintable" summary="This table displays Tab Items." cellspacing="0" cellpadding="0" border="0">
<tbody><tr>
<td class="taboff" height="22">
<a href="/pls/PROD/twbkwbis.P_GenMenu?name=bmenu.P_GenMnu" onmouseover="window.status='Personal Information'; return true" onmouseout="window.status=''; return true" onfocus="window.status='Personal Information'; return true" onblur="window.status=''; return true">Kişisel Bilgiler</a>
</td>
<td class="bgtaboff" height="22" valign="top" align="right">
<img src="/wtlgifs/web_tab_corner_right.gif" alt="Tab Corner Right" class="headerImg" title="Tab Corner Right" name="web_tab_corner_right" hspace="0" vspace="0" border="0" height="20" width="8">
</td>
<td class="taboff" height="22">
<a href="/pls/PROD/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu" onmouseover="window.status='Student Services &amp; Financial Aid'; return true" onmouseout="window.status=''; return true" onfocus="window.status='Student Services &amp; Financial Aid'; return true" onblur="window.status=''; return true">Öğrenci Servisi</a>
</td>
<td class="bgtaboff" height="22" valign="top" align="right">
<img src="/wtlgifs/web_tab_corner_right.gif" alt="Tab Corner Right" class="headerImg" title="Tab Corner Right" name="web_tab_corner_right" hspace="0" vspace="0" border="0" height="20" width="8">
</td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td class="bgtabon" width="100%" colspan="2"><img src="/wtlgifs/web_transparent.gif" alt="Transparent Image" class="headerImg" title="Transparent Image" name="web_transparent" hspace="0" vspace="0" border="0" height="3" width="10"></td></tr></tbody></table>
</map>
</span>
<a name="skip_Module_Navigation_Links_H"></a>
</div>
<table class="plaintable" summary="This table displays Menu Items and Banner Search textbox." width="100%">
<tbody><tr>
<td class="pldefault">
<div class="headerlinksdiv2">
<form action="/pls/PROD/twbksrch.P_ShowResults" method="POST">
Search
<span class="fieldlabeltextinvisible"><label for="keyword_in_id"><span class="fieldlabeltext">Search</span></label></span>
<input type="text" name="KEYWRD_IN" size="20" maxlength="65" id="keyword_in_id">
<input type="submit" value="Go">
</form>
</div>
</td>
<td class="pldefault"><p class="rightaligntext">
<span class="pageheaderlinks">
<a href="/pls/PROD/twbksite.P_DispSiteMap?menu_name_in=bmenu.P_MainMnu&amp;depth_in=2&amp;columns_in=3" accesskey="2" class="submenulinktext2">SITE MAP</a>
|
<a href="/wtlhelp/twbhhelp.htm" accesskey="H" onclick="popup = window.open('/wtlhelp/twbhhelp.htm', 'PopupPage','height=450,width=500,scrollbars=yes,resizable=yes'); return false" target="_blank" onmouseover="window.status='';  return true" onmouseout="window.status=''; return true" onfocus="window.status='';  return true" onblur="window.status=''; return true" class="submenulinktext2">HELP</a>
|
<a href="twbkwbis.P_Logout" accesskey="3" class="submenulinktext2">EXIT</a>
</span>
</p></td>
</tr>
</tbody></table>
</div>
<div class="pagetitlediv">
<table class="plaintable" summary="This table displays title and static header displays." width="100%">
<tbody><tr>
<td class="pldefault">
&nbsp;
</td>
<td class="pldefault">
&nbsp;
</td>
<td class="pldefault"><p class="rightaligntext">
</p><div class="staticheaders">
090150727 Sevim Şenacay<br>
Aug 11, 2018 10:42 pm<br>
</div>
</td>
</tr>
<tr>
<td class="bg3" width="100%" colspan="3"><img src="/wtlgifs/web_transparent.gif" alt="Transparent Image" class="headerImg" title="Transparent Image" name="web_transparent" hspace="0" vspace="0" border="0" height="3" width="10"></td>
</tr>
</tbody></table>
<a name="main_content"></a>
</div>
<div class="pagebodydiv">
<!--  ** END OF twbkwbis.P_OpenDoc **  -->

<table width="750" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" align="center">
<tbody><tr>
<td>
<table width="100%" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr><td class="default"><img src="http://resimler.sis.itu.edu.tr/090/15/0727.jpg" height="100"></td>
</tr><tr>
<td width="150"><font face="ARIAL" size="2" color="#013C5B"><b>Ögrenci No</b></font></td>
<td width="225"><font face="ARIAL" size="2" color="#013C5B">:&nbsp;090150727</font></td>
<td width="150"><font face="ARIAL" size="2" color="#013C5B"><b>TC Kimlik No</b></font></td>
<td width="225"><font face="ARIAL" size="2" color="#013C5B">:&nbsp;36115658522</font></td>
</tr>
<tr>
<td><font face="ARIAL" size="2" color="#013C5B"><b>Soyadi</b></font></td>
<td><font face="ARIAL" size="2" color="#013C5B">:&nbsp;Şenacay</font></td>
<td><font face="ARIAL" size="2" color="#013C5B"><b>Seviye</b></font></td>
<td><font face="ARIAL" size="2" color="#013C5B">:&nbsp;Lisans</font></td>
</tr>
<tr>
<td><font face="ARIAL" size="2" color="#013C5B"><b>Adi</b></font></td>
<td><font face="ARIAL" size="2" color="#013C5B">:&nbsp;Sevim </font></td>
<td></td>
<td></td>
</tr>
<tr>
<td><font face="ARIAL" size="2" color="#013C5B"><b>Dogum Yeri</b></font></td>
<td><font face="ARIAL" size="2" color="#013C5B">:&nbsp;Bayrampaşa</font></td>
<td></td>
<td></td>
</tr>
<tr>
<td><font face="ARIAL" size="2" color="#013C5B"><b>Dogum Tarihi</b></font></td>
<td><font face="ARIAL" size="2" color="#013C5B">:&nbsp;30-06-1995</font></td>
<td><font face="ARIAL" size="2" color="#013C5B"><b>Kayit Tarihi</b></font></td>
<td><font face="ARIAL" size="2" color="#013C5B">:&nbsp;04-09-2015</font></td>
</tr>
<tr>
<td><font face="ARIAL" size="2" color="#013C5B"><b>Baba Adi</b></font></td>
<td><font face="ARIAL" size="2" color="#013C5B">:&nbsp;Gürkan</font></td>
<td><font face="ARIAL" size="2" color="#013C5B"><b>Kayit Tipi</b></font></td>
<td><font face="ARIAL" size="2" color="#013C5B">:&nbsp;Merkezi Y.P.Dış Yatay Geçiş</font></td>
</tr>
</tbody></table>
<br>
<table width="100%" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2015-2016 / Güz</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BIL 101E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Int to Comp and Inf Systems</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.50&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 110</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Fizik Mühendisliğine Giriş</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">AA </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 113</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Mekanik</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   4.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 113EL</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Mechanics Laboratory</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">ING 101</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">English I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 101</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Matematik I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   5.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  15.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   5.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  15.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  12.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 0.77</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  15.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   5.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  15.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  12.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 0.77</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B">Gözetim Listesi</font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2015-2016 / Bahar</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">ALM 102</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Almanca II (Kredisiz)</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   0.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BZ </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BIL 101E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Int to Comp and Inf Systems</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.50&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 113</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Mekanik</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   4.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DD </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 114EL</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Continous Media Laboratory</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CB </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">KIM 101E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">General Chemistry I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 101</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Matematik I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   5.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">RUS 101</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Rusça I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   0.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BL </font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  14.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  14.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  14.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  25.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.76</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  30.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  19.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  19.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  37.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.92</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B">İyi Durum</font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2015-2016 / Yaz Öğretimi</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BIL 106E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Intr to Sci&amp;Eng Comp (Fortran)</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DD </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">ING 102</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">English II</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 102</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Matematik II</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   5.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  11.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   6.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  11.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   9.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 0.82</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  41.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  25.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  30.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  46.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.52</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B">Gözetim Listesi</font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2016-2017 / Güz</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">ATA 101</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Atatürk İlk &amp; İnkılap Trh I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   2.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CB </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BEB 101</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Temel Yüzme Becerisi Öğrenimi</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   0.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BZ *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 213</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Elektrik ve Manyetizma</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   4.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DD *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 233E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Electronics I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 233EL</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Electronics I Lab.</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 241E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Symblc &amp; Numrc Tchnqs in Physc</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   2.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">KIM 101EL</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">General Chemistry I Lab</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">AA </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 102</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Matematik II</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   5.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  18.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  10.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  18.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  17.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 0.97</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  59.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  35.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  43.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  64.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.47</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B">Gözetim Listesi</font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2016-2017 / Bahar</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BEB 101</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Temel Yüzme Becerisi Öğrenimi</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   0.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">VF </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DNK 201E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Dynamics</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 213E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Electricity and Magnetism</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   4.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 213EL</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Electricity &amp; Magnetism Lab.</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BA </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 292E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Computer Aided Dsgn &amp; Modellng</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   2.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">AA </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">ITB 218</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Bilim ve Teknoloji Tarihi</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CB </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 102</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Matematik II</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   5.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  18.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  13.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  18.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  29.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.64</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  77.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  44.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  52.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  89.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.70</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B">Gözetim Listesi</font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2016-2017 / Yaz Öğretimi</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">ATA 102</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Atatürk İlk &amp; İnkılap Trh II</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   2.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CB </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 241E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Symblc &amp; Numrc Tchnqs in Physc</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   2.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 102</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Matematik II</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   5.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BB </font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   9.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   9.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   9.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  23.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 2.56</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  86.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  53.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  54.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 112.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 2.06</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B">İyi Durum</font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2017-2018 / Güz</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BEB 116</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Badminton Temel Beceri Eğitimi</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   0.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">VF </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 114</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Sürekli Ortamlar Fiziği</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 233EL</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Electronics I Lab.</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BB </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 284</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Klasik Mekanik I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 210</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Mühendislik Matematiği</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   4.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DD </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 261</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Lineer Cebir</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DD </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">MAT 335E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Programming Algorithms</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF </font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  17.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   8.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  17.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  10.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 0.59</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 103.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  61.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  70.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 122.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.74</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B">Gözetim Listesi</font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2017-2018 / Bahar</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 114</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Sürekli Ortamlar Fiziği</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">DC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 284E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Classical Mechanics I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 321E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Mathematical Mthds in Physc I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   4.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">VF </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 374E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Methods of Experim.Physics I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FF *</font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 443E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Solar Energy Physics &amp;Tech. I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BA </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">TUR 102</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Türk Dili II</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   2.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CB </font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  18.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   8.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  18.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  20.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.11</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 121.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  69.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  82.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 142.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.73</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B">Gözetim Listesi</font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" bgcolor="lightgray"><b><font face="ARIAL" size="2" color="#013C5B">2017-2018 / Yaz Öğretimi</font></b></td>
</tr>
<tr>
<td valign="top" width="400">
<table border="0" cellspacing="0" cellpadding="0" bordercolor="#000000" width="100%">
<tbody><tr>
<td width="75" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Ders Kodu</font></b></td>
<td width="255"><b><font face="ARIAL" size="2" color="#013C5B">Ders Adi</font></b></td>
<td width="35" nowrap="" align="right"><b><font face="ARIAL" size="2" color="#013C5B">Kredi&nbsp;</font></b></td>
<td width="35" nowrap=""><b><font face="ARIAL" size="2" color="#013C5B">Not</font></b></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 272E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Computatnl Methods in Physics</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BB </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 374E</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Methods of Experim.Physics I</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   3.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">CC </font></td>
</tr>
<tr>
<td width="75" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">FIZ 374EL</font></td>
<td width="255" valign="top"><font face="ARIAL" size="2" color="#013C5B">Methods of Exp. Physics Lab.</font></td>
<td width="35" nowrap="" align="right" valign="top"><font face="ARIAL" size="2" color="#013C5B">   1.00&nbsp;</font></td>
<td width="35" nowrap="" valign="top"><font face="ARIAL" size="2" color="#013C5B">BA </font></td>
</tr>
</tbody></table>
</td>
<td valign="top" width="350" align="right">
<table width="350" border="0" cellspacing="0" cellpadding="0" bordercolor="#000000">
<tbody><tr>
<td width="100"></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>A.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>O.K.Krd.</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>B.Puan</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"><b>Ort.</b></font></td>
</tr>
<tr>
<td colspan="6"><font face="ARIAL" size="2" color="#013C5B"><b>Fizik Mühendisliği</b></font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Dönem</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   7.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   7.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">   7.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  18.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 2.64</font></td>
</tr>
<tr>
<td width="50"><font face="ARIAL" size="2" color="#013C5B"><b>Toplam</b></font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 128.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  76.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B">  86.50</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 161.00</font></td>
<td width="50" align="right"><font face="ARIAL" size="2" color="#013C5B"> 1.86</font></td>
</tr>
<tr>
<td width="100"><font face="ARIAL" size="2" color="#013C5B"><b>Akd. Durum</b></font></td>
<td colspan="5" width="250"><font face="ARIAL" size="2" color="#013C5B"></font></td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td align="center"><font face="ARIAL" size="2" color="#013C5B">**Belge Sonu**</font></td>
</tr>
<tr>
<td align="right"><font face="ARIAL" size="2" color="#013C5B">Belge Tarihi:11-08-2018</font></td>
</tr>
</tbody></table>



<!--  ** START OF twbkwbis.P_CloseDoc **  -->
<table class="plaintable" summary="This is table displays line separator at end of the page." width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="bgtabon" width="100%" colspan="2"><img src="/wtlgifs/web_transparent.gif" alt="Transparent Image" class="headerImg" title="Transparent Image" name="web_transparent" hspace="0" vspace="0" border="0" height="3" width="10"></td></tr></tbody></table>
<a href="#top" onmouseover="window.status='Skip to top of page'; return true" onmouseout="window.status=''; return true" onfocus="window.status='Skip to top of page'; return true" onblur="window.status=''; return true" class="skiplinks">Skip to top of page</a>

<div class="pagefooterdiv">
<span class="releasetext">Release: 8.4</span>
</div>
<div class="poweredbydiv">
</div>
<div class="div1"></div>
<div class="div2"></div>
<div class="div3"></div>
<div class="div4"></div>
<div class="div5"></div>
<div class="div6"></div>


</td></tr></tbody></table></div></body></html>
"""