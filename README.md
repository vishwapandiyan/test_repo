# Test Repository for DevGuard Security Scanner

This is a test repository containing intentional security vulnerabilities for testing the DevGuard security scanning tool.

## ⚠️ WARNING

**DO NOT USE THIS CODE IN PRODUCTION!**

This repository contains intentional security vulnerabilities including:
- Hardcoded API keys and secrets
- SQL injection vulnerabilities
- Insecure Firebase rules
- Open security group configurations
- .env file committed to repository

## Purpose

This repository is designed to test security scanning tools like DevGuard. All security issues are intentional for demonstration purposes.

## Files with Security Issues

- `app.py` - Hardcoded secrets, SQL injection, eval usage
- `.env` - Environment file with secrets (should never be committed)
- `firebase.json` - Open Firebase security rules
- `config.py` - Hardcoded credentials and weak encryption
- `aws_config.yml` - Open security groups allowing public access

## How to Use for Testing

1. Upload this repository to GitHub (as a public or private repo)
2. Run DevGuard scanner on this repository
3. DevGuard should detect all the intentional security issues

