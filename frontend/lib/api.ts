// API configuration and utility functions

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export interface Property {
  id: number;
  address: string;
  city: string;
  state: string;
  zip_code: string;
  price: number;
  bedrooms: number;
  bathrooms: number;
  square_feet: number;
  property_type: string;
  year_built: number;
}

// Fetch all properties
export async function getProperties(): Promise<Property[]> {
  const response = await fetch(`${API_BASE_URL}/api/v1/properties`, {
    cache: "no-store", // Always fetch fresh data
  });

  if (!response.ok) {
    throw new Error("Failed to fetch properties");
  }

  return response.json();
}

// Fetch a single property by ID
export async function getProperty(id: number): Promise<Property> {
  const response = await fetch(`${API_BASE_URL}/api/v1/properties/${id}`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(`Failed to fetch property ${id}`);
  }

  return response.json();
}

