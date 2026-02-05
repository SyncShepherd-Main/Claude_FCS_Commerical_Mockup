/* ============================================
   FCS COMMERCIAL SERVICES - SHARED JAVASCRIPT
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {

  /* --- FAQ ACCORDION --- */
  document.querySelectorAll('.faq-question').forEach(function(question) {
    question.addEventListener('click', function() {
      var item = this.parentElement;
      var toggle = this.querySelector('.faq-toggle');
      var wasActive = item.classList.contains('active');
      
      document.querySelectorAll('.faq-item').forEach(function(i) {
        i.classList.remove('active');
        var t = i.querySelector('.faq-toggle');
        if (t) t.textContent = '+';
      });
      
      if (!wasActive) {
        item.classList.add('active');
        if (toggle) toggle.textContent = '−';
      }
    });
  });

  /* --- MOBILE NAV TOGGLE --- */
  var navToggle = document.querySelector('.nav-toggle');
  var navList = document.querySelector('.nav-list');
  
  if (navToggle && navList) {
    navToggle.addEventListener('click', function() {
      navList.classList.toggle('active');
      this.textContent = navList.classList.contains('active') ? '✕' : '☰';
    });
  }

  /* --- MOBILE DROPDOWN TOGGLE --- */
  if (window.innerWidth <= 900) {
    document.querySelectorAll('.nav-list > li').forEach(function(li) {
      var dropdown = li.querySelector('.nav-dropdown');
      if (dropdown) {
        li.querySelector('a').addEventListener('click', function(e) {
          if (this.getAttribute('href') === '#') {
            e.preventDefault();
            dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
          }
        });
      }
    });
  }

  /* --- ACTIVE NAV STATE --- */
  var currentPath = window.location.pathname;
  document.querySelectorAll('.nav-list a').forEach(function(link) {
    if (link.getAttribute('href') === currentPath) {
      link.closest('li').classList.add('active');
    }
  });

});
