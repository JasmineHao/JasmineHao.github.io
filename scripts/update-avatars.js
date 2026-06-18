const fs = require('fs');
const path = require('path');

const avatarsDir = path.join(__dirname, '..', 'avatars');
const indexPath = path.join(__dirname, '..', 'index.html');

const files = fs.readdirSync(avatarsDir)
  .filter(f => /\.(png|jpe?g|webp|gif)$/i.test(f))
  .sort()
  .map(f => `    "/avatars/${f}"`);

const avatarsBlock = `  const avatars = [\n${files.join(',\n')}\n  ];`;

let html = fs.readFileSync(indexPath, 'utf8');
const startMarker = '/* AVATARS_START */';
const endMarker = '/* AVATARS_END */';

if (!html.includes(startMarker)) {
  const regex = /const avatars = \[[\s\S]*?\];/;
  if (!regex.test(html)) {
    console.error('Could not find avatars array in index.html');
    process.exit(1);
  }
  html = html.replace(regex, `${startMarker}\n${avatarsBlock}\n${endMarker}`);
} else {
  const regex = new RegExp(`${startMarker}[\\s\\S]*?${endMarker}`);
  html = html.replace(regex, `${startMarker}\n${avatarsBlock}\n${endMarker}`);
}

fs.writeFileSync(indexPath, html);
console.log(`Updated avatars list with ${files.length} images.`);
