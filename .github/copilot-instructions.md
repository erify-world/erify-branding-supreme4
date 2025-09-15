# ERIFY™ Supreme 4 Branding Repository Instructions

ALWAYS follow these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information provided here.

## Repository Overview
ERIFY™ Supreme 4 Branding Repository is a static HTML branding site that showcases the ERIFY™ Supreme 4 Crest Banner and Neon Crown Series assets. The site is deployed via GitHub Pages and features vector-first branding assets with PNG/WEBP exports.

## Working Effectively

### Build and Deploy Process
- Build the site: `./build.sh` -- takes 0.02 seconds. NEVER CANCEL.
- Serve locally: `python3 -m http.server 8000 --directory public` -- serves instantly
- All assets load in under 0.01 seconds per file
- Complete site build and deployment: under 1 minute including GitHub Actions

### Required Dependencies
- Python 3 (pre-installed in GitHub Actions runners)
- Pillow (for image generation): `pip install Pillow` -- takes 30 seconds. NEVER CANCEL.
- No Node.js, npm, or complex build tools required

### Repository Structure
```
.
├── .github/workflows/pages-deploy.yml  # GitHub Pages deployment
├── build.sh                           # Build script (18ms execution time)
├── src/
│   ├── pages/
│   │   ├── index.html                 # Main HTML page
│   │   └── favicon.svg                # Site favicon  
│   ├── css/
│   │   └── erify-glow-kit.css        # ERIFY branding CSS
│   └── svg/
│       └── crest-supreme4.svg        # Main vector logo
├── dist/                             # Generated image assets
│   ├── crest-supreme4-full.png       # Main banner image
│   ├── crest-supreme4.png           # Standard logo
│   ├── crest-supreme4.webp          # WEBP versions
│   └── neon-*.png                   # Neon series images
└── public/                          # Built site (auto-generated)
```

## Validation Scenarios

### CRITICAL: Always Test Complete User Scenarios
1. **Build and Serve Test**:
   ```bash
   ./build.sh
   python3 -m http.server 8000 --directory public
   curl -s http://localhost:8000/ | head -5  # Verify HTML loads
   ```

2. **Asset Loading Test**:
   ```bash
   curl -s -o /dev/null -w "CSS: %{http_code} " http://localhost:8000/css/erify-glow-kit.css
   curl -s -o /dev/null -w "IMG: %{http_code} " http://localhost:8000/dist/crest-supreme4-full.png
   curl -s -o /dev/null -w "SVG: %{http_code}\n" http://localhost:8000/svg/crest-supreme4.svg
   ```
   Expected output: `CSS: 200 IMG: 200 SVG: 200`

3. **Download Functionality Test**:
   ```bash
   curl -s -o /dev/null -w "PNG: %{http_code}\n" http://localhost:8000/dist/crest-supreme4.png
   curl -s -o /dev/null -w "WEBP: %{http_code}\n" http://localhost:8000/dist/crest-supreme4.webp
   curl -s -o /dev/null -w "SVG: %{http_code}\n" http://localhost:8000/svg/crest-supreme4.svg
   ```
   Expected output: All should return `200`

## Build Commands and Timing

### CRITICAL: Build Times and Timeout Values
- `./build.sh` -- 0.02 seconds execution time. NEVER CANCEL. Set timeout to 60+ seconds.
- `pip install Pillow` -- 30 seconds. NEVER CANCEL. Set timeout to 120+ seconds.
- Local server startup -- instant. No timeout needed.
- GitHub Actions deployment -- 2-3 minutes total. NEVER CANCEL. Set timeout to 10+ minutes.

### Exact Commands to Build and Test
```bash
# 1. Build the site
chmod +x build.sh
./build.sh

# 2. Test locally  
python3 -m http.server 8000 --directory public &
SERVER_PID=$!

# 3. Validate all components
sleep 2
curl -s -o /dev/null -w "Site load: %{time_total}s, Status: %{http_code}\n" http://localhost:8000/

# 4. Test downloads
curl -s -o /tmp/test.png http://localhost:8000/dist/crest-supreme4.png
curl -s -o /tmp/test.webp http://localhost:8000/dist/crest-supreme4.webp  
curl -s -o /tmp/test.svg http://localhost:8000/svg/crest-supreme4.svg

# 5. Cleanup
kill $SERVER_PID
```

## Deployment Process

### GitHub Pages Deployment
The site auto-deploys via GitHub Actions on push to main branch:
1. Checkout code
2. Run `./build.sh` 
3. Deploy `./public` directory to gh-pages branch
4. Site available at: `https://erify-world.github.io/erify-branding-supreme4/`

### Manual Deployment Validation
```bash
# Test the exact build process used by GitHub Actions
git checkout main
./build.sh
ls -la public/  # Verify all files present
python3 -m http.server 8000 --directory public  # Test serving
```

## Development Workflow

### Making Changes
1. **HTML changes**: Edit `src/pages/index.html`
2. **Styling changes**: Edit `src/css/erify-glow-kit.css` 
3. **New images**: Add to `dist/` directory
4. **Vector assets**: Add to `src/svg/` directory
5. **Always rebuild**: Run `./build.sh` after any changes
6. **Always test**: Serve locally and validate functionality

### Asset Generation
If you need to create new placeholder images:
```python
# Install Pillow first: pip install Pillow
python3 -c "
from PIL import Image, ImageDraw, ImageFont
def create_placeholder(filename, size, text, bg_color='#0A0B0C', text_color='#11C9FF'):
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    draw.text((x, y), text, fill=text_color, font=font)
    draw.rectangle([20, 20, size[0]-20, size[1]-20], outline='#FFD700', width=3)
    img.save(f'dist/{filename}')
    print(f'Created dist/{filename}')
create_placeholder('new-image.png', (600, 300), 'NEW IMAGE')
"
```

## CI/CD Validation

### Before Committing Changes
```bash
# ALWAYS run these validation steps:
./build.sh                                   # Build takes 0.02s
python3 -m http.server 8000 --directory public &  # Start server  
sleep 2
curl -s http://localhost:8000/ > /dev/null   # Test main page
curl -s http://localhost:8000/css/erify-glow-kit.css > /dev/null  # Test CSS
curl -s http://localhost:8000/dist/crest-supreme4-full.png > /dev/null  # Test images
pkill -f "python3 -m http.server"           # Stop server
echo "✅ All validation passed"
```

## Common Operations

### Repository Root Contents
```
ls -la /
.
..
.git/
.github/
.gitignore
README.md
build.sh
src/
dist/  
public/
```

### Build Script Output
```bash
./build.sh
# Expected output:
🔨 Building ERIFY™ Supreme 4 Branding Site...
📄 Copying HTML files...
🎨 Copying CSS files...
🖼️  Copying image assets...
✅ Build complete! Site ready in ./public directory
🚀 Serve locally with: python3 -m http.server 8000 --directory public
📊 Build took [timestamp]
```

### Site Load Testing Results
- **HTML page**: 4827 bytes, loads in 0.006s
- **CSS file**: 1387 bytes, loads instantly  
- **Main banner**: PNG ~50KB, loads in 0.01s
- **All assets**: Complete site loads in under 0.1s
- **Build time**: 0.02s consistently
- **Server startup**: Instant

## Troubleshooting

### Common Issues
1. **404 on assets**: Run `./build.sh` to regenerate public directory
2. **CSS not loading**: Check `src/css/erify-glow-kit.css` exists
3. **Images missing**: Verify all files exist in `dist/` directory
4. **Build fails**: Ensure `build.sh` has execute permissions: `chmod +x build.sh`
5. **Server won't start**: Kill existing process: `pkill -f "python3 -m http.server"`

### GitHub Actions Failing
- Check that `./build.sh` runs locally without errors
- Verify `public/` directory is created and contains all files
- Ensure workflow has correct publish_dir: `./public`

## Key Files Reference

### build.sh
Main build script that copies all source files to public directory for deployment.

### src/pages/index.html  
Main HTML page with ERIFY branding showcase. Uses relative paths for all assets.

### src/css/erify-glow-kit.css
ERIFY brand styling with glow effects, neon colors, and responsive design.

### .github/workflows/pages-deploy.yml
GitHub Actions workflow for automatic deployment to GitHub Pages.

ALWAYS validate your changes work by running the complete build and test process before committing.