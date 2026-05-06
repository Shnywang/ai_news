const fs = require('fs');
const path = require('path');
const dataDir = path.join(__dirname, 'data');
const cutoff = Date.now() - 7 * 86400000;
const files = fs.readdirSync(dataDir).filter(f => /^\d{4}-\d{2}-\d{2}/.test(f) && f.endsWith('.json'));
files.forEach(f => {
  const fp = path.join(dataDir, f);
  const stat = fs.statSync(fp);
  if (stat.mtimeMs < cutoff) {
    console.log('Deleting:', f);
    fs.unlinkSync(fp);
  } else {
    console.log('Keeping:', f);
  }
});
console.log('Cleanup done.');
