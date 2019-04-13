let map;
let infowindow;

function initMap() {
    let datos = [
        {
            "title": "Marcador 1",
            "lat": 20.975507,
            "long": -89.622176,
            "description": "Es una prueba de marcador"
        },
        {
            "title": "Marcador 2",
            "lat": 20.975600,
            "long": -89.622200,
            "description": "Es una prueba de marcador"
        }
    ]
    cargarMapa();
    /* envia los JSON de la informacion */
    cargarMarcador(datos);
}

function cargarMarcador(datos) {
    datos.forEach(elemento => {
        let location = new google.maps.LatLng(elemento.lat, elemento.long)
        let marker = new google.maps.Marker({
            position: location,
            map: map,
            titulo: elemento.title
        });
        
        google.maps.event.addListener(marker, 'click', (e) => {
            infowindow = new google.maps.InfoWindow({
                content:marker.titulo
            });
            infowindow.open(map,marker);
        });
    });
}

function cargarMapa() {
    let posicion = new google.maps.LatLng(20.975507, -89.622176);
    map = new google.maps.Map(document.getElementById('map'), {
        streetViewControl: true,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.LEFT_TOP
        },
        disableDefaultUI: true,
        center: posicion,
        zoom: 15,
        styles: [
            { elementType: 'geometry', stylers: [{ color: '#242f3e' }] },
            { elementType: 'labels.text.stroke', stylers: [{ color: '#242f3e' }] },
            { elementType: 'labels.text.fill', stylers: [{ color: '#746855' }] },
            {
                featureType: 'administrative.locality',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }]
            },
            {
                featureType: 'poi',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }]
            },
            {
                featureType: 'poi.park',
                elementType: 'geometry',
                stylers: [{ color: '#263c3f' }]
            },
            {
                featureType: 'poi.park',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#6b9a76' }]
            },
            {
                featureType: 'road',
                elementType: 'geometry',
                stylers: [{ color: '#38414e' }]
            },
            {
                featureType: 'road',
                elementType: 'geometry.stroke',
                stylers: [{ color: '#212a37' }]
            },
            {
                featureType: 'road',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#9ca5b3' }]
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry',
                stylers: [{ color: '#746855' }]
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry.stroke',
                stylers: [{ color: '#1f2835' }]
            },
            {
                featureType: 'road.highway',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#f3d19c' }]
            },
            {
                featureType: 'transit',
                elementType: 'geometry',
                stylers: [{ color: '#2f3948' }]
            },
            {
                featureType: 'transit.station',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }]
            },
            {
                featureType: 'water',
                elementType: 'geometry',
                stylers: [{ color: '#17263c' }]
            },
            {
                featureType: 'water',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#515c6d' }]
            },
            {
                featureType: 'water',
                elementType: 'labels.text.stroke',
                stylers: [{ color: '#17263c' }]
            }
        ]
    });
}