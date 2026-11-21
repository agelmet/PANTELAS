(function(){
var D=document,H=D.documentElement,RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
var T={en:{t:'Taxi & VIP chauffeur transfers in Athens | GP & GP',d:'GP & GP: taxi, a 7-seater for up to 6 passengers and VIP Mercedes, BMW, Audi — always with a driver. Athens, Nea Smyrni, Piraeus, airports, day trips, by the hour or up to 7 days.'}};
var lang='el';try{lang=localStorage.getItem('gp-lang')||'el'}catch(e){}
var TEL='{{TEL1}}',TEL2='{{TEL2}}',M1='{{MAIL1}}',M2='{{MAIL2}}';
/* ---- language ---- */
var ATTR=[['data-en-alt','alt'],['data-en-aria','aria-label'],['data-en-ph','placeholder']];
function setLang(l){lang=l;try{localStorage.setItem('gp-lang',l)}catch(e){}
 H.lang=l;
 D.querySelectorAll('[data-en]').forEach(function(e){if(e.dataset.el==null)e.dataset.el=e.innerHTML;e.innerHTML=l==='en'?e.dataset.en:e.dataset.el});
 ATTR.forEach(function(p){D.querySelectorAll('['+p[0]+']').forEach(function(e){var k='el'+p[1].replace(/\W/g,'');if(e.dataset[k]==null)e.dataset[k]=e.getAttribute(p[1])||'';e.setAttribute(p[1],l==='en'?e.getAttribute(p[0]):e.dataset[k])})});
 D.querySelectorAll('.lng button').forEach(function(b){b.classList.toggle('on',b.dataset.l===l)});
 if(l==='en'){D.title=T.en.t}else if(window.__elT){D.title=__elT}
 splitAll();words();ticket();stepLbl();
}
window.__elT=D.title;
D.querySelectorAll('.lng button').forEach(function(b){b.addEventListener('click',function(){if(b.dataset.l!==lang){H.classList.add('lswap');setLang(b.dataset.l)}})});
/* ---- headings: letter cascade ---- */
function splitH(h){var i=0;function walk(n){Array.from(n.childNodes).forEach(function(c){if(c.nodeType===3){var f=D.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(w){if(!w)return;if(/^\s+$/.test(w)){f.appendChild(D.createTextNode(' '));return}var ws=D.createElement('span');ws.className='cw';Array.from(w).forEach(function(ch){var s=D.createElement('span');s.className='ch';s.style.setProperty('--i',i++);s.textContent=ch;ws.appendChild(s)});f.appendChild(ws)});c.replaceWith(f)}else if(c.nodeType===1&&c.tagName!=='BR')walk(c)})}walk(h)}
function splitAll(){D.querySelectorAll('.lc-h').forEach(function(h){h.setAttribute('aria-label',h.textContent.replace(/\s+/g,' ').trim());splitH(h)})}
/* ---- hero words ---- */
function words(){var d=D.getElementById('dsp');if(!d)return;var html='',i=0;
 function wrapText(t){return t.split(/(\s+)/).map(function(w){if(!w)return'';if(/^\s+$/.test(w))return' ';return'<span class="wm"><span class="w"><span style="transition-delay:'+(0.35+0.07*(i++))+'s">'+w+'</span></span></span>'}).join('')}
 Array.from(d.childNodes).forEach(function(c){if(c.nodeType===3)html+=wrapText(c.textContent);else if(c.tagName==='EM'){html+='<em>'+wrapText(c.textContent)+'<svg class="ul" viewBox="0 0 100 6" preserveAspectRatio="none" aria-hidden="true"><path d="M1 4 C 30 1, 70 1, 99 3" pathLength="1"/></svg></em>'}});
 d.innerHTML=html}
/* ---- reveals ---- */
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.04});
function watch(){D.querySelectorAll('.rv,.rvt,.lc-h').forEach(function(e){if(!e.classList.contains('in'))io.observe(e)})}
/* ---- intro ---- */
function start(){H.classList.add('go')}
var intro=D.getElementById('intro'),seen=false;try{seen=sessionStorage.getItem('gp-intro')}catch(e){}
if(!RM&&!D.hidden&&!seen&&intro){intro.hidden=false;try{sessionStorage.setItem('gp-intro','1')}catch(e){}
 setTimeout(function(){intro.classList.add('out');setTimeout(start,300)},1650);
 setTimeout(function(){intro.hidden=true},2600)}
else{requestAnimationFrame(function(){setTimeout(start,60)})}
setTimeout(start,3200);
/* ---- header, progress, parallax, journey (one rAF scroll handler) ---- */
var hd=D.querySelector('.hd'),prog=D.querySelector('.prog'),tt=D.querySelector('.totop'),mb=D.querySelector('.mbar'),wedbg=D.querySelector('.wed .bg'),wed=D.querySelector('.wed'),cue=D.querySelector('.scue');
var steps=D.querySelector('.steps'),rail=steps&&steps.querySelector('.rail i'),car=steps&&steps.querySelector('.car'),sts=steps?[].slice.call(steps.querySelectorAll('.st')):[],imgs=[].slice.call(D.querySelectorAll('.stage img')),cur=0,tick=false;
function stepLbl(){var s=sts[cur];if(!s)return;var b=D.getElementById('stb');if(b)b.textContent=lang==='en'?s.dataset.te:s.dataset.t;var n=D.getElementById('sts');if(n)n.textContent='0'+(cur+1)+' / 0'+sts.length}
function onScroll(){tick=false;var y=scrollY,vh=innerHeight,h=D.documentElement.scrollHeight-vh;
 hd.classList.toggle('solid',y>40);var p=h>0?y/h:0;H.style.setProperty('--sp',p.toFixed(4));
 tt.classList.toggle('on',y>vh*1.2);mb.classList.toggle('on',y>vh*.55);if(cue)cue.style.opacity=y>40?0:1;
 if(wed&&!RM){var r=wed.getBoundingClientRect();if(r.bottom>0&&r.top<vh){wedbg.style.setProperty('--py',((r.top+r.height/2-vh/2)*-.12).toFixed(1)+'px')}}
 if(steps){var r2=steps.getBoundingClientRect(),line=vh*.55,q=Math.min(1,Math.max(0,(line-r2.top)/r2.height));rail.parentNode.style.setProperty('--p',q.toFixed(4));rail.style.setProperty('--p',q.toFixed(4));car.style.setProperty('--cy',(q*(r2.height-40)).toFixed(1)+'px');
  var a=0;sts.forEach(function(s,i){if(s.getBoundingClientRect().top<line)a=i});if(a!==cur){cur=a;sts.forEach(function(s,i){s.classList.toggle('on',i===a)});imgs.forEach(function(m,i){m.classList.toggle('on',i===a)});stepLbl()}}
}
addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});addEventListener('resize',onScroll);
/* ---- hero pointer light ---- */
var hero=D.querySelector('.hero');if(hero&&matchMedia('(hover:hover)').matches&&!RM){hero.addEventListener('pointermove',function(e){var r=hero.getBoundingClientRect();hero.style.setProperty('--gx',((e.clientX-r.left)/r.width*100).toFixed(1)+'%');hero.style.setProperty('--gy',((e.clientY-r.top)/r.height*100).toFixed(1)+'%')})}
/* ---- service tilt + spotlight ---- */
if(matchMedia('(hover:hover)').matches&&!RM){D.querySelectorAll('.sv').forEach(function(c){var box;c.addEventListener('pointerenter',function(){box=c.getBoundingClientRect()});c.addEventListener('pointermove',function(e){if(!box)return;var x=(e.clientX-box.left)/box.width,y=(e.clientY-box.top)/box.height;c.style.setProperty('--mx',x*100+'%');c.style.setProperty('--my',y*100+'%');c.style.transform='perspective(900px) rotateX('+((.5-y)*5).toFixed(2)+'deg) rotateY('+((x-.5)*6).toFixed(2)+'deg) translateY(-4px)'});c.addEventListener('pointerleave',function(){c.style.transform=''})})}
/* ---- mobile nav ---- */
var bg=D.querySelector('.burger'),mn=D.querySelector('.mnav');
function openM(o){if(o){mn.hidden=false;requestAnimationFrame(function(){mn.classList.add('open')});[].forEach.call(mn.querySelectorAll('a.l'),function(a,i){a.style.transitionDelay=(.05+i*.05)+'s'})}else{mn.classList.remove('open');setTimeout(function(){mn.hidden=true},400)}bg.setAttribute('aria-expanded',o);D.body.style.overflow=o?'hidden':''}
bg.addEventListener('click',function(){openM(true)});mn.querySelector('.x').addEventListener('click',function(){openM(false)});mn.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){openM(false)})});
/* ---- lightbox ---- */
var lb=D.querySelector('.lb'),lbi=lb.querySelector('img'),lbp=lb.querySelector('p');
function openLB(src,alt){lbi.src=src;lbi.alt=alt||'';lbp.textContent=alt||'';lb.hidden=false;requestAnimationFrame(function(){lb.classList.add('on')})}
function closeLB(){lb.classList.remove('on');setTimeout(function(){lb.hidden=true;lbi.src=''},350)}
D.querySelectorAll('.gal figure').forEach(function(f){f.addEventListener('click',function(){var i=f.querySelector('img');openLB(f.dataset.big,i.alt)})});
D.querySelectorAll('.sv .ph img,.st .mimg img,.wed .bg img').forEach(function(i){i.style.cursor='zoom-in';i.addEventListener('click',function(){openLB((i.currentSrc||i.src),i.alt)})});
lb.addEventListener('click',function(e){if(e.target===lb||e.target.closest('.x'))closeLB()});
addEventListener('keydown',function(e){if(e.key==='Escape'){if(!lb.hidden)closeLB();if(mn.classList.contains('open'))openM(false)}});
/* ---- FAQ: one open ---- */
var dts=[].slice.call(D.querySelectorAll('#faq details'));dts.forEach(function(d){d.addEventListener('toggle',function(){if(d.open)dts.forEach(function(o){if(o!==d)o.open=false})})});
/* ---- booking composer ---- */
var svc='taxi',days='1',L={el:{taxi:'Ταξί',seven:'Επταθέσιο',vip:'VIP αυτοκίνητο',days:'Ενοικίαση με οδηγό',event:'Γάμος / εκδήλωση',d:' ημέρ',hi:'Καλησπέρα σας! Θα ήθελα να κλείσω:',from:'Από',to:'Προς',when:'Πότε',pax:'Επιβάτες',dd:'Διάρκεια',note:'Σημείωση',cp:'Το μήνυμα αντιγράφηκε — κάντε επικόλληση στο Viber.',subj:'Κράτηση διαδρομής'},
 en:{taxi:'Taxi',seven:'7-seater',vip:'VIP car',days:'Hire with driver',event:'Wedding / event',d:' day',hi:'Hello! I would like to book:',from:'From',to:'To',when:'When',pax:'Passengers',dd:'Duration',note:'Note',cp:'Message copied — paste it in Viber.',subj:'Ride booking'}};
function $(i){return D.getElementById(i)}
function chips(id,cb){var w=$(id);w.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;w.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});cb(b.dataset.v)})}
function setSvc(v){svc=v;$('svcs').querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x.dataset.v===v)});$('g-days').hidden=!(v==='days'||v==='seven'||v==='vip'||v==='event');ticket()}
chips('svcs',setSvc);chips('days',function(v){days=v;$('g-hrs').hidden=v!=='h';ticket()});$('f-hrs').addEventListener('change',ticket);
D.querySelectorAll('[data-svc]').forEach(function(a){a.addEventListener('click',function(){setSvc(a.dataset.svc)})});
['f-from','f-to','f-date','f-time','f-pax','f-note'].forEach(function(i){$(i).addEventListener('input',ticket)});
function fmtDate(v){if(!v)return'';var p=v.split('-');return p[2]+'/'+p[1]+'/'+p[0]}
function dur(){if($('g-days').hidden)return'';var t=L[lang];if(days==='h'){var h=$('f-hrs').value;return h+(lang==='el'?(h==='1'?' ώρα':' ώρες'):(h==='1'?' hour':' hours'))}return days+(lang==='el'?(days==='1'?' ημέρα':' ημέρες'):(days==='1'?' day':' days'))}
function set(id,v){var e=$(id);e.textContent=v||'—';e.classList.toggle('e',!v)}
function ticket(){if(!$('t-svc'))return;var t=L[lang];var s=t[svc]+(dur()?' · '+dur():'');set('t-svc',s);set('t-from',$('f-from').value.trim());set('t-to',$('f-to').value.trim());var w=[fmtDate($('f-date').value),$('f-time').value].filter(Boolean).join(' · ');set('t-when',w);set('t-pax',$('f-pax').value)}
function msg(){var t=L[lang],o=[t.hi,'• '+t[svc]+(dur()?' ('+t.dd+': '+dur()+')':'')];var f=$('f-from').value.trim(),to=$('f-to').value.trim(),w=[fmtDate($('f-date').value),$('f-time').value].filter(Boolean).join(' '),n=$('f-note').value.trim();
 if(f)o.push(t.from+': '+f);if(to)o.push(t.to+': '+to);if(w)o.push(t.when+': '+w);o.push(t.pax+': '+$('f-pax').value);if(n)o.push(t.note+': '+n);return o.join('\n')}
function toast(s){var c=D.querySelector('.copied');c.textContent=s;c.classList.add('on');setTimeout(function(){c.classList.remove('on')},3200)}
function copy(s){try{navigator.clipboard.writeText(s)}catch(e){var a=D.createElement('textarea');a.value=s;D.body.appendChild(a);a.select();try{D.execCommand('copy')}catch(x){}a.remove()}}
$('s-wa').addEventListener('click',function(){open('https://wa.me/'+TEL.replace(/\D/g,'')+'?text='+encodeURIComponent(msg()),'_blank','noopener')});
$('s-vb').addEventListener('click',function(){copy(msg());toast(L[lang].cp);setTimeout(function(){location.href='viber://chat?number=%2B'+TEL.replace(/\D/g,'')},500)});
$('s-sms').addEventListener('click',function(){location.href='sms:'+TEL+'?&body='+encodeURIComponent(msg())});
$('s-ml').addEventListener('click',function(){location.href='mailto:'+M1+'?cc='+M2+'&subject='+encodeURIComponent(L[lang].subj+' — GP & GP')+'&body='+encodeURIComponent(msg())});
/* ---- the card ---- */
var c3=$('card3'),fx=c3&&c3.querySelector('.fx'),fy=0,drag=null;
function setF(v){fy=v;c3.style.setProperty('--fy',fy+'deg')}
$('flip').addEventListener('click',function(){setF(fy+180)});
c3.addEventListener('click',function(){if(!drag||Math.abs(drag.dx)<6)setF(fy+180)});
c3.addEventListener('pointerdown',function(e){drag={x:e.clientX,f:fy,dx:0};c3.style.transition='none';fx.style.transition='none'});
addEventListener('pointermove',function(e){if(!drag)return;drag.dx=e.clientX-drag.x;if(Math.abs(drag.dx)>6)c3.style.setProperty('--fy',(drag.f+drag.dx*.6)+'deg')});
addEventListener('pointerup',function(){if(!drag)return;c3.style.transition='';fx.style.transition='';if(Math.abs(drag.dx)>6){setF(Math.round((drag.f+drag.dx*.6)/180)*180)}setTimeout(function(){drag=null},20)});
if(matchMedia('(hover:hover)').matches&&!RM){var cw=D.querySelector('.cardw');cw.addEventListener('pointermove',function(e){if(drag)return;var r=cw.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c3.style.setProperty('--ry',(x*22).toFixed(1)+'deg');c3.style.setProperty('--rx',(-y*16).toFixed(1)+'deg');c3.querySelectorAll('.face').forEach(function(f){f.style.setProperty('--sx',(x*80)+'%')})});cw.addEventListener('pointerleave',function(){c3.style.setProperty('--ry','-14deg');c3.style.setProperty('--rx','8deg')})}
var cio=new IntersectionObserver(function(es){if(es[0].isIntersecting&&!RM){setTimeout(function(){setF(fy+180)},900);setTimeout(function(){setF(fy+180)},3200);cio.disconnect()}},{threshold:.5});cio.observe(c3);
$('vcf').addEventListener('click',function(){var v=['BEGIN:VCARD','VERSION:3.0','N:;GP & GP;;;','FN:GP & GP · Taxi & VIP Transfer','ORG:GP & GP','TITLE:Taxi · VIP Transfer','TEL;TYPE=CELL,VOICE:'+TEL,'TEL;TYPE=CELL,VOICE:'+TEL2,'EMAIL;TYPE=INTERNET:'+M1,'EMAIL;TYPE=INTERNET:'+M2,'URL:'+location.origin+location.pathname,'NOTE:Viber · WhatsApp','END:VCARD'].join('\r\n');var a=D.createElement('a');a.href=URL.createObjectURL(new Blob([v],{type:'text/vcard'}));a.download='GP-and-GP.vcf';D.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},500)});
/* ---- boot ---- */
D.querySelectorAll('[data-en]').forEach(function(e){e.dataset.el=e.innerHTML});
if(lang==='en')setLang('en');else{splitAll();words();ticket();stepLbl()}
watch();onScroll();
})();
