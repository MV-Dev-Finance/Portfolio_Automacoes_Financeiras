document.querySelectorAll('.fbtn').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('on'));b.classList.add('on');const f=b.dataset.f;document.querySelectorAll('.pcard').forEach(c=>{c.style.display=(f==='all'||c.dataset.area===f)?'':'none'})}));
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('on'));t.classList.add('on');document.querySelectorAll('.frame img').forEach((im,i)=>im.classList.toggle('on',i==t.dataset.i))}));
const lb=document.getElementById('lb');
document.querySelectorAll('.gi,.iash img').forEach(el=>el.addEventListener('click',()=>{const src=el.dataset.full||el.getAttribute('src');lb.querySelector('img').src=src;lb.classList.add('on')}));
lb.addEventListener('click',()=>lb.classList.remove('on'));document.addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('on')});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
