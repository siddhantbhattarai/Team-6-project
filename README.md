# Team-6-project
# Software Requirements Specification (SRS) for Kavyalaya.com

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to provide a detailed software requirements specification (SRS) for the development of Kavyalaya.com, a platform where users can create profiles, post various types of literature, and interact with each other through following, commenting, liking, and sharing posts.

### 1.2 Scope
Kavyalaya.com will enable users to:
- Create and customize profiles.
- Post literature in various categories.
- Follow other users/authors.
- Share, comment, and like posts.
- Verify their email to sign up.
- Log in via email.
- Use enhanced features such as notifications, content categorization, search functionality, bookmarks, rating system, content recommendations, editor tools, collaborative writing, events and contests, user levels and badges, analytics, subscription model, language support, monetization options, content moderation, and integration with social media.

### 1.3 Definitions, Acronyms, and Abbreviations
- **SRS**: Software Requirements Specification
- **OS**: Operating System
- **HTML**: HyperText Markup Language
- **CSS**: Cascading Style Sheets
- **SQL**: Structured Query Language
- **API**: Application Programming Interface
- **SSL**: Secured Socket Layer

### 1.4 References
- Django Documentation: https://docs.djangoproject.com/
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- Docker Documentation: https://docs.docker.com/
- Ubuntu Documentation: https://help.ubuntu.com/

## 2. Overall Description

### 2.1 Product Perspective
Kavyalaya.com is a standalone web application designed to foster a community of literature enthusiasts. It is a new product built from scratch using the Django framework for the backend, HTML/CSS for the frontend, PostgreSQL for the database, Docker for containerization, and Ubuntu 24.04 as the operating system.

### 2.2 Product Features
- **User Profiles**: Users can create and customize their profiles.
- **Literature Posting**: Users can post literature in various categories.
- **Email Verification**: Users must verify their email to sign up.
- **Email Login**: Users can log in via email.
- **Follow Functionality**: Users can follow other users/authors.
- **Interactions**: Users can share, comment on, and like posts.
- **Notifications**: Users receive notifications for new followers, likes, comments, and shares.
- **Content Categorization**: Posts can be tagged and categorized.
- **Search Functionality**: Users can search for posts, authors, and categories.
- **Bookmarks**: Users can bookmark or favorite posts.
- **Rating System**: Posts can be rated.
- **Content Recommendations**: Recommended posts and authors based on user activity.
- **Editor Tools**: Rich text or markdown editors for creating posts.
- **Collaborative Writing**: Multiple users can collaborate on a single piece of writing.
- **Events and Contests**: Literature events, contests, and challenges.
- **User Levels and Badges**: Gamification with user levels and badges.
- **Analytics**: Analytics on posts for authors.
- **Subscription Model**: Premium features or ad-free experience.
- **Language Support**: Multi-language support.
- **Monetization Options**: Monetize content through donations, paid subscriptions, or selling works.
- **Content Moderation**: Reporting and moderating inappropriate content.
- **Social Media Integration**: Share posts on social media platforms.

### 2.3 User Classes and Characteristics
- **General Users**: Users who can read, share, comment, and like posts.
- **Authors**: Users who can post literature and engage with followers.
- **Administrators**: Users who manage and moderate the platform.

### 2.4 Operating Environment
- **Backend**: Python/Django
- **Frontend**: HTML/CSS
- **Database**: PostgreSQL, SQLite(For Testing)
- **Containerization & Scaling**: Docker/Kubernetes
- **Processing Manager**: PM2
- **Operating System**: Ubuntu 24.04
- **Deployment**: Oracle Cloud
- **Storage**: Oracle Bucket
- **CDN**: Cloudflare
- **Caching**: Redis
- **Monitoring**: Prometheus, Logging, Sentry
- **Security**: SSL/TLS, CloudFlare Firewall
- **Networking**: Cloudflare One (Zero Trust)
- **Backup & Recovery**: Backup Strategies (Periodic Snapshot Backups)
- **Development Practices**: Version Control (Git)
- **CI/CD**: Github Actions
- **User Interface**: Design Tools (Figma)

### 2.5 Design and Implementation Constraints
- The application must be built using the specified technology stack.
- The system should ensure data security and user privacy.
- The application should be scalable to handle a growing number of users and posts.

### 2.6 Assumptions and Dependencies
- Users have access to a stable internet connection.
- Users have basic knowledge of operating web applications.
- The development team is familiar with the chosen technology stack.

## 3. Specific Requirements

### 3.1 Functional Requirements
- **User Registration and Authentication**:
  - Users can register with their email and must verify their email to complete registration.
  - Users can log in using their email and password.
  
- **User Profiles**:
  - Users can create and customize their profiles with avatars, bios, and cover photos.
  
- **Literature Posting**:
  - Users can post literature in various categories.
  - Posts can be tagged and categorized.
  
- **Interactions**:
  - Users can follow other users/authors.
  - Users can like, comment on, and share posts.
  - Users can bookmark or favorite posts.
  
- **Notifications**:
  - Users receive notifications for new followers, likes, comments, and shares.
  
- **Content Discovery**:
  - Users can search for posts, authors, and categories.
  - Users receive content recommendations based on their interests.
  
- **Editor Tools**:
  - Provide rich text or markdown editors for creating posts.
  
- **Collaborative Writing**:
  - Allow multiple users to collaborate on a single piece of writing.
  
- **Events and Contests**:
  - Organize literature events, contests, and challenges.
  
- **User Levels and Badges**:
  - Introduce a gamification element with user levels and badges.
  
- **Analytics**:
  - Provide authors with analytics on their posts, such as views, likes, shares, and comments.
  
- **Subscription Model**:
  - Offer premium features or a subscription model for advanced features or ad-free experience.
  
- **Language Support**:
  - Provide multi-language support.
  
- **Monetization Options**:
  - Allow authors to monetize their content through donations, paid subscriptions, or selling their works.
  
- **Content Moderation**:
  - Implement a system for reporting and moderating inappropriate content.
  
- **Social Media Integration**:
  - Enable sharing of posts on social media platforms.

### 3.2 Non-Functional Requirements
- **Performance**: The system should handle high traffic and large volumes of data efficiently.
- **Security**: Ensure data security and user privacy.
- **Usability**: The platform should be user-friendly and easy to navigate.
- **Scalability**: The system should be scalable to accommodate growth in users and content.
- **Reliability**: The application should be reliable and have minimal downtime.
- **Maintainability**: The codebase should be maintainable and well-documented.

## 4. External Interface Requirements

### 4.1 User Interfaces
- **Web Interface**: Accessible via standard web browsers.

### 4.2 Hardware Interfaces
- Not applicable.

### 4.3 Software Interfaces
- **Email Service**: For sending verification and notification emails.
- **Payment Gateway**: For handling transactions related to monetization options and subscriptions.
- **Social Media APIs**: For integrating social media sharing functionalities.

### 4.4 Communication Interfaces
- **HTTP/HTTPS**: For secure communication between the client and server.