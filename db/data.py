# Sample data storage (in production, this would be a database)
events_db = [
    {
        "id": 1,
        "title": "Kubernetes Workshop",
        "date": "2024-11-15",
        "speaker": "John Doe",
        "description": "Learn Kubernetes from scratch",
        "status": "upcoming"
    },
    {
        "id": 2,
        "title": "Docker Deep Dive",
        "date": "2024-10-20",
        "speaker": "Jane Smith",
        "description": "Advanced Docker concepts",
        "status": "completed"
    }
]


team_members = [
    {"name": "John Doe", "role": "Organizer", "bio": "Cloud Native enthusiast"},
    {"name": "Jane Smith", "role": "Co-Organizer", "bio": "Kubernetes expert"},
    {"name": "Bob Wilson", "role": "Community Lead", "bio": "DevOps advocate"}
]


resources = [
    {"title": "Getting Started with Kubernetes", "link": "#", "type": "Tutorial"},
    {"title": "Introduction to Cloud Native", "link": "#", "type": "Article"},
    {"title": "CNCF Landscape", "link": "#", "type": "Reference"}
]


blog_posts = [
    {
        "id": 1,
        "title": "Getting Started with Kubernetes in Nepal",
        "slug": "getting-started-kubernetes-nepal",
        "author": "John Doe",
        "date": "2024-10-15",
        "excerpt": "An introductory guide to Kubernetes for developers in Nepal. Learn the basics and set up your first cluster.",
        "content": """
        <p>Kubernetes has become the de facto standard for container orchestration, and the cloud native ecosystem in Nepal is growing rapidly. In this post, we'll explore how you can get started with Kubernetes and join our thriving community.</p>

        <h2>Why Kubernetes?</h2>
        <p>Kubernetes provides automated deployment, scaling, and management of containerized applications. It's essential for modern cloud native development.</p>

        <h2>Getting Started</h2>
        <p>First, you'll need to install kubectl and set up a local cluster using Minikube or Kind. Here are the steps:</p>
        <ol>
            <li>Install Docker on your machine</li>
            <li>Install kubectl command-line tool</li>
            <li>Set up Minikube for local development</li>
            <li>Deploy your first application</li>
        </ol>

        <h2>Join Our Community</h2>
        <p>We host regular workshops and meetups in Kathmandu. Join us to learn more and connect with fellow cloud native enthusiasts!</p>
        """
    },
    {
        "id": 2,
        "title": "Cloud Native Security Best Practices",
        "slug": "cloud-native-security-best-practices",
        "author": "Jane Smith",
        "date": "2024-10-08",
        "excerpt": "Security is paramount in cloud native environments. Discover essential practices to secure your Kubernetes clusters.",
        "content": """
        <p>As cloud native adoption grows, security becomes increasingly critical. This guide covers essential security practices for your Kubernetes deployments.</p>

        <h2>Key Security Principles</h2>
        <p>Cloud native security follows several core principles that you should implement:</p>

        <h3>1. Least Privilege Access</h3>
        <p>Always grant the minimum permissions necessary. Use RBAC (Role-Based Access Control) to manage access to your cluster resources.</p>

        <h3>2. Network Policies</h3>
        <p>Implement network policies to control traffic between pods. This provides an additional layer of security beyond traditional firewalls.</p>

        <h3>3. Image Scanning</h3>
        <p>Scan your container images for vulnerabilities before deployment. Tools like Trivy and Clair can help automate this process.</p>

        <h2>Secrets Management</h2>
        <p>Never hardcode secrets in your applications. Use Kubernetes Secrets or external secret management tools like HashiCorp Vault.</p>
        """
    },
    {
        "id": 3,
        "title": "Introduction to Service Mesh with Istio",
        "slug": "introduction-service-mesh-istio",
        "author": "Bob Wilson",
        "date": "2024-09-28",
        "excerpt": "Service meshes are revolutionizing microservices architecture. Learn how Istio can help manage your service-to-service communication.",
        "content": """
        <p>Service meshes have become an essential component of modern microservices architectures. In this post, we'll explore Istio, one of the most popular service mesh implementations.</p>

        <h2>What is a Service Mesh?</h2>
        <p>A service mesh is a dedicated infrastructure layer for handling service-to-service communication. It provides features like traffic management, security, and observability without requiring changes to your application code.</p>

        <h2>Why Istio?</h2>
        <p>Istio offers several compelling features:</p>
        <ul>
            <li>Traffic management with advanced routing rules</li>
            <li>Automatic mutual TLS for service-to-service communication</li>
            <li>Built-in observability with metrics, logs, and traces</li>
            <li>Policy enforcement and rate limiting</li>
        </ul>

        <h2>Getting Started with Istio</h2>
        <p>Installing Istio on your Kubernetes cluster is straightforward. We'll cover the installation process and deploy a sample application in our next workshop.</p>
        """
    }
]


