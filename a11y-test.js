// Accessibility test file
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.createElement('button');
  btn.innerHTML = 'Click me';
  // Missing aria-label on icon button
  var icon = document.createElement('span');
  icon.className = 'icon';
  btn.appendChild(icon);
  document.body.appendChild(btn);

  var img = document.createElement('img');
  img.src = 'logo.png';
  // Missing alt attribute
  document.body.appendChild(img);
});
