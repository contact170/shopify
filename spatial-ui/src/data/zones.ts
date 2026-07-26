export type ZoneId = 'entree' | 'fenetres' | 'couloir' | 'salon' | 'garage' | 'jardin';

export interface ZoneContent {
  id: ZoneId;
  eyebrow: string;
  title: string;
  description: string;
  price: string;
  sku: string;
  image: string;
  link: string;
}

// Fallback content used only if a merchant hasn't filled in the section's
// "zone" blocks yet in the theme editor. SKUs, prices and photos are the
// real Daewoo Security catalog, taken from sections/Daewoo-quizz.liquid so
// nothing on the hero is a placeholder.
export const DEFAULT_ZONES: Record<ZoneId, ZoneContent> = {
  entree: {
    id: 'entree',
    eyebrow: 'Entrée',
    title: 'Contacteur de porte',
    description: "Détecte chaque ouverture, en silence, jour et nuit.",
    price: '39,90 €',
    sku: 'WDV301',
    image:
      'https://cdn.shopify.com/s/files/1/0326/3132/4811/products/camera-interieure-rotative-daewoo-ip506p-wifi-full-hd-vie-privee-645500.webp?v=1767965265',
    link: '/collections/systeme-d-alarme'
  },
  fenetres: {
    id: 'fenetres',
    eyebrow: 'Fenêtres',
    title: 'Détecteur de vibration',
    description: 'Repère un choc ou une tentative d’effraction avant l’intrusion.',
    price: '34,90 €',
    sku: 'WVD301',
    image:
      'https://cdn.shopify.com/s/files/1/0326/3132/4811/products/camera-interieure-rotative-daewoo-ip506p-wifi-full-hd-vie-privee-645500.webp?v=1767965265',
    link: '/collections/systeme-d-alarme'
  },
  couloir: {
    id: 'couloir',
    eyebrow: 'Couloir',
    title: 'Détecteur de mouvement',
    description: 'Couvre le passage, compatible animaux de compagnie.',
    price: '34,90 €',
    sku: 'WPS305',
    image:
      'https://cdn.shopify.com/s/files/1/0326/3132/4811/products/camera-interieure-rotative-daewoo-ip506p-wifi-full-hd-vie-privee-645500.webp?v=1767965265',
    link: '/collections/systeme-d-alarme'
  },
  salon: {
    id: 'salon',
    eyebrow: 'Salon',
    title: 'Caméra intérieure rotative',
    description: 'Vision Full HD, suit le mouvement, respecte votre vie privée.',
    price: '69,90 €',
    sku: 'IP506P',
    image:
      'https://cdn.shopify.com/s/files/1/0326/3132/4811/products/camera-interieure-rotative-daewoo-ip506p-wifi-full-hd-vie-privee-645500.webp?v=1767965265',
    link: '/collections/cameras'
  },
  garage: {
    id: 'garage',
    eyebrow: 'Garage',
    title: 'Contacteur porte de garage',
    description: 'Renforcé pour les grandes ouvertures, résiste aux vibrations du moteur.',
    price: '49,90 €',
    sku: 'WDG301',
    image:
      'https://cdn.shopify.com/s/files/1/0326/3132/4811/files/OFFRESPECIAL_7.png?v=1772203809',
    link: '/collections/systeme-d-alarme'
  },
  jardin: {
    id: 'jardin',
    eyebrow: 'Jardin & terrasse',
    title: 'Sirène extérieure 110 dB',
    description: "S'active en moins d'une seconde et prévient tout le voisinage.",
    price: '129,90 €',
    sku: 'WOS305S',
    image:
      'https://cdn.shopify.com/s/files/1/0326/3132/4811/files/OFFRESPECIAL_8.png?v=1772204007',
    link: '/collections/systeme-d-alarme'
  }
};

export const ZONE_ORDER: ZoneId[] = ['entree', 'fenetres', 'couloir', 'salon', 'garage', 'jardin'];
