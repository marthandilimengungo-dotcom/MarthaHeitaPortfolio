# Web Deployment Guide - Martha Heita Portfolio

## Overview
This guide covers deploying your Flet portfolio application to the web for public access.

## Deployment Options

### Option 1: Flet Cloud (Recommended - Easiest)

#### Step 1: Create Flet Cloud Account
1. Go to https://flet.io/
2. Sign up for free account
3. Verify email

#### Step 2: Install Flet CLI
```bash
pip install flet-cli
```

#### Step 3: Deploy
```bash
flet publish portfolio.py
```

**Output:**
- Your portfolio will be available at: `https://flet.io/your-app-name`
- Public URL ready to share
- Auto-updates with code changes

### Option 2: GitHub Pages (Static Deployment)

#### Step 1: Build Static Files
```bash
flet build web
```

#### Step 2: Configure GitHub Pages
1. Go to repository Settings → Pages
2. Select source: `Deploy from a branch`
3. Select branch: `gh-pages`
4. Select folder: `/root`

#### Step 3: Push to GitHub
```bash
git add .
git commit -m "Deploy portfolio to GitHub Pages"
git push origin main
```

**Output:**
- Portfolio available at: `https://marthandilimengungo-dotcom.github.io/MarthaHeitaPortfolio`

### Option 3: Heroku Deployment

#### Step 1: Create Heroku Account
- Sign up at https://www.heroku.com

#### Step 2: Install Heroku CLI
```bash
# macOS
brew tap heroku/brew && brew install heroku

# Windows/Linux
# Download from https://devcenter.heroku.com/articles/heroku-cli
```

#### Step 3: Create Procfile
```bash
echo "web: flet run portfolio.py --web" > Procfile
```

#### Step 4: Create requirements.txt
```bash
pip freeze > requirements.txt
```

#### Step 5: Deploy
```bash
heroku login
heroku create martha-heita-portfolio
git push heroku main
```

**Output:**
- Portfolio available at: `https://martha-heita-portfolio.herokuapp.com`

### Option 4: Docker + AWS/Google Cloud

#### Step 1: Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080
EXPOSE 8080

CMD ["flet", "run", "portfolio.py", "--web", "--port", "8080"]
```

#### Step 2: Build Image
```bash
docker build -t martha-portfolio .
```

#### Step 3: Deploy to Cloud
- **Google Cloud Run:** Push to Google Container Registry
- **AWS ECS:** Push to Amazon ECR
- **Azure:** Push to Azure Container Registry

## Quick Deployment Comparison

| Option | Ease | Cost | Setup Time |
|--------|------|------|-----------|
| Flet Cloud | ⭐⭐⭐⭐⭐ | FREE | 5 min |
| GitHub Pages | ⭐⭐⭐⭐ | FREE | 10 min |
| Heroku | ⭐⭐⭐ | FREE (limited) | 15 min |
| Docker/AWS | ⭐⭐ | $$ | 30 min |

## Recommended: Flet Cloud Deployment (Step-by-Step)

### Step 1: Install Dependencies
```bash
pip install flet flet-cli
```

### Step 2: Test Locally First
```bash
flet run portfolio.py
# Verify everything works at http://localhost:8000
```

### Step 3: Publish to Flet Cloud
```bash
flet publish portfolio.py
```

### Step 4: Follow Prompts
```
Enter app name: martha-heita-portfolio
Select account: (select your Flet Cloud account)
```

### Step 5: Get Your URL
Your portfolio is now live at:
```
https://flet.io/apps/martha-heita-portfolio
```

## Post-Deployment

### Update Your Portfolio
To make changes and redeploy:

```bash
# Make code changes
# Commit to GitHub
git add .
git commit -m "Update portfolio content"
git push origin main

# Republish to Flet Cloud
flet publish portfolio.py --force
```

### Monitor Deployment
- Check app status: Flet Cloud Dashboard
- View logs: `flet logs portfolio.py`
- Check performance: Flet Analytics

## Environment Variables

If you need configuration:

```bash
# Create .env file
echo "PORTFOLIO_ENV=production" > .env

# Deploy with env variables
flet publish portfolio.py --env PORTFOLIO_ENV=production
```

## Custom Domain (Optional)

For production portfolio on custom domain:

1. **Flet Cloud:**
   - Go to app settings
   - Add custom domain
   - Update DNS records

2. **GitHub Pages:**
   - Create CNAME file with domain
   - Update DNS to point to GitHub

3. **Heroku:**
   - Add domain in app settings
   - Update DNS records

## SSL/HTTPS Certificate

All platforms provide free SSL certificates:
- ✅ Flet Cloud: Automatic
- ✅ GitHub Pages: Automatic
- ✅ Heroku: Automatic
- ✅ AWS/Google Cloud: Automatic

## Monitoring & Analytics

### Flet Cloud Dashboard
- View app visitors
- Check performance metrics
- Monitor error logs
- View deployment history

### GitHub Pages Stats
- Traffic analytics in repository
- Deployment status
- Build logs

## Troubleshooting Deployment

### "Port already in use"
```bash
flet run portfolio.py --port 8081
```

### "Module not found"
```bash
pip install -r requirements.txt
flet publish portfolio.py
```

### "Build failed"
```bash
# Clear cache
rm -rf .flet
flet publish portfolio.py --force
```

### "Can't access portfolio"
- Check deployment status in dashboard
- Verify URL is correct
- Wait 30 seconds for deployment to complete
- Clear browser cache (Ctrl+F5)

## Performance Optimization

For faster deployment:

```bash
# Minimize Python files
pip install pyminify

# Optimize images
pip install pillow-simd

# Clear unnecessary files before deploy
rm -rf __pycache__ .git/hooks
```

## Backup & Version Control

Always keep GitHub updated:

```bash
# Before each deployment
git add .
git commit -m "Deploy version X.X"
git push origin main
```

## Next Steps

1. ✅ Choose deployment option (recommend: Flet Cloud)
2. ✅ Deploy portfolio to web
3. ✅ Share portfolio URL with instructors
4. ✅ Monitor performance
5. ✅ Update portfolio as needed

## Support & Resources

- **Flet Documentation:** https://flet.io/docs
- **GitHub Pages Guide:** https://pages.github.com
- **Heroku Dev Center:** https://devcenter.heroku.com
- **Docker Hub:** https://hub.docker.com

---

**Deployment Status Checklist:**
- [ ] Dependencies installed
- [ ] Local testing completed
- [ ] Deployment platform chosen
- [ ] App deployed to web
- [ ] URL verified and working
- [ ] Portfolio accessible publicly
- [ ] Instructors notified with URL

**Portfolio URL (after deployment):** 
```
https://[deployment-platform]/martha-heita-portfolio
```

