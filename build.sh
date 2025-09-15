#!/bin/bash
# ERIFY™ Branding Supreme4 - Build Script
# Builds the static site for deployment to GitHub Pages

set -e

echo "🔨 Building ERIFY™ Supreme 4 Branding Site..."

# Clean and create public directory
rm -rf public
mkdir -p public/{css,dist,svg}

# Copy HTML pages
echo "📄 Copying HTML files..."
cp src/pages/*.html public/
cp src/pages/*.svg public/

# Copy CSS files
echo "🎨 Copying CSS files..."
cp src/css/* public/css/

# Copy assets
echo "🖼️  Copying image assets..."
cp dist/* public/dist/
cp src/svg/* public/svg/

echo "✅ Build complete! Site ready in ./public directory"
echo "🚀 Serve locally with: python3 -m http.server 8000 --directory public"
echo "📊 Build took $(date)"