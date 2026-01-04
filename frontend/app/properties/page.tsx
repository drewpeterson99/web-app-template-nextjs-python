import Link from "next/link";
import { getProperties } from "@/lib/api";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Alert,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/alert";

export default async function PropertiesPage() {
  let properties;
  let error = null;

  try {
    properties = await getProperties();
  } catch (err) {
    error = err instanceof Error ? err.message : "Failed to example data";
  }

  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <Button asChild variant="ghost">
            <Link href="/">← Back to Home</Link>
          </Button>
          <h1 className="mt-4 text-4xl font-bold">Example Data</h1>
          <p className="mt-2 text-lg text-muted-foreground">
            Browse example data cards
          </p>
        </div>

        {error ? (
          <Alert variant="destructive">
            <AlertTitle>Error example data</AlertTitle>
            <AlertDescription>
              <p className="mt-1">{error}</p>
              <p className="mt-2">
                Make sure your backend server is running on{" "}
                {process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000"}
              </p>
            </AlertDescription>
          </Alert>
        ) : (
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {properties?.map((property) => (
              <Card key={property.id} className="hover:shadow-lg transition-shadow">
                <CardHeader>
                  <CardTitle className="text-xl">{property.address}</CardTitle>
                  <CardDescription>
                    {property.city}, {property.state} {property.zip_code}
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-2">
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Price:</span>
                      <span className="font-semibold">
                        ${property.price.toLocaleString()}
                      </span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Bedrooms:</span>
                      <span>{property.bedrooms}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Bathrooms:</span>
                      <span>{property.bathrooms}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Square Feet:</span>
                      <span>{property.square_feet.toLocaleString()}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Type:</span>
                      <span>{property.property_type}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Year Built:</span>
                      <span>{property.year_built}</span>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

