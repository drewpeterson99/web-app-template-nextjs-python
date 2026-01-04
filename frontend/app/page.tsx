import Link from "next/link";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background">
      <main className="flex w-full max-w-4xl flex-col items-center justify-center px-8 py-16">
        <div className="w-full space-y-8 text-center">
          <div className="space-y-4">
            <h1 className="text-5xl font-bold tracking-tight sm:text-6xl">
              Example Web Application Home Page
            </h1>
            <p className="mx-auto max-w-2xl text-xl leading-8 text-muted-foreground">
              Next.js frontend with Python + FastAPI backend
            </p>
          </div>

          <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Link href="/properties">
              <Button size="lg">View Example Data</Button>
            </Link>
            <a
              href="http://127.0.0.1:8000/docs"
              target="_blank"
              rel="noopener noreferrer"
            >
              <Button variant="outline" size="lg">API Documentation</Button>
            </a>
          </div>

          <div className="mt-16 grid gap-6 sm:grid-cols-3">
            <Card>
              <CardHeader>
                <CardTitle>Card 1 Title</CardTitle>
                <CardDescription>
                  Card 1 description
                </CardDescription>
              </CardHeader>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Card 2 Title</CardTitle>
                <CardDescription>
                  Card 2 description
                </CardDescription>
              </CardHeader>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Card 3 Title</CardTitle>
                <CardDescription>
                  Card 3 description
                </CardDescription>
              </CardHeader>
            </Card>
          </div>
        </div>
      </main>
    </div>
  );
}
