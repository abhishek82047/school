import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace title
html = html.replace('<title>About - Time Public School</title>', '<title>Gallery - Time Public School</title>')
html = html.replace('About Time Public School', 'School Gallery')
html = html.replace('A Legacy of Excellence in Education', 'Moments Captured in Time')

# Replace the About Content section with Gallery section
gallery_section = """
    <!-- Gallery Content -->
    <section class="section-padding bg-white pt-5">
        <div class="container">
            <div class="section-title text-center mb-5">
                <span class="text-secondary fw-bold text-uppercase d-block mb-2" style="letter-spacing: 2px;">Our Memories</span>
                <h2>Campus Photo Gallery</h2>
                <p class="text-muted mx-auto" style="max-width: 600px;">A glimpse into the vibrant academic and co-curricular life at Time Public School.</p>
            </div>
            
            <div class="row g-4">
                <!-- Gallery Item 1 -->
                <div class="col-lg-4 col-md-6">
                    <div class="gallery-item rounded-4 overflow-hidden shadow-sm position-relative">
                        <img src="assets/images/school image.jpeg" alt="Campus View" class="w-100 img-fluid" style="height: 250px; object-fit: cover; transition: transform 0.3s ease;">
                        <div class="gallery-overlay position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center bg-dark bg-opacity-50 opacity-0" style="transition: opacity 0.3s ease;">
                            <span class="text-white fw-bold fs-5">Campus View</span>
                        </div>
                    </div>
                </div>
                <!-- Gallery Item 2 -->
                <div class="col-lg-4 col-md-6">
                    <div class="gallery-item rounded-4 overflow-hidden shadow-sm position-relative">
                        <img src="assets/images/school image.jpeg" alt="Science Lab" class="w-100 img-fluid" style="height: 250px; object-fit: cover; transition: transform 0.3s ease;">
                        <div class="gallery-overlay position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center bg-dark bg-opacity-50 opacity-0" style="transition: opacity 0.3s ease;">
                            <span class="text-white fw-bold fs-5">Science Lab</span>
                        </div>
                    </div>
                </div>
                <!-- Gallery Item 3 -->
                <div class="col-lg-4 col-md-6">
                    <div class="gallery-item rounded-4 overflow-hidden shadow-sm position-relative">
                        <img src="assets/images/school image.jpeg" alt="Sports Day" class="w-100 img-fluid" style="height: 250px; object-fit: cover; transition: transform 0.3s ease;">
                        <div class="gallery-overlay position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center bg-dark bg-opacity-50 opacity-0" style="transition: opacity 0.3s ease;">
                            <span class="text-white fw-bold fs-5">Sports Day</span>
                        </div>
                    </div>
                </div>
                <!-- Gallery Item 4 -->
                <div class="col-lg-4 col-md-6">
                    <div class="gallery-item rounded-4 overflow-hidden shadow-sm position-relative">
                        <img src="assets/images/school image.jpeg" alt="Annual Function" class="w-100 img-fluid" style="height: 250px; object-fit: cover; transition: transform 0.3s ease;">
                        <div class="gallery-overlay position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center bg-dark bg-opacity-50 opacity-0" style="transition: opacity 0.3s ease;">
                            <span class="text-white fw-bold fs-5">Annual Function</span>
                        </div>
                    </div>
                </div>
                <!-- Gallery Item 5 -->
                <div class="col-lg-4 col-md-6">
                    <div class="gallery-item rounded-4 overflow-hidden shadow-sm position-relative">
                        <img src="assets/images/school image.jpeg" alt="Library" class="w-100 img-fluid" style="height: 250px; object-fit: cover; transition: transform 0.3s ease;">
                        <div class="gallery-overlay position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center bg-dark bg-opacity-50 opacity-0" style="transition: opacity 0.3s ease;">
                            <span class="text-white fw-bold fs-5">Digital Library</span>
                        </div>
                    </div>
                </div>
                <!-- Gallery Item 6 -->
                <div class="col-lg-4 col-md-6">
                    <div class="gallery-item rounded-4 overflow-hidden shadow-sm position-relative">
                        <img src="assets/images/school image.jpeg" alt="Classroom" class="w-100 img-fluid" style="height: 250px; object-fit: cover; transition: transform 0.3s ease;">
                        <div class="gallery-overlay position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center bg-dark bg-opacity-50 opacity-0" style="transition: opacity 0.3s ease;">
                            <span class="text-white fw-bold fs-5">Smart Classrooms</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <style>
                .gallery-item:hover img { transform: scale(1.1) !important; }
                .gallery-item:hover .gallery-overlay { opacity: 1 !important; }
            </style>
        </div>
    </section>
"""

start_marker = "<!-- About Content -->"
end_marker = "<!-- Shared Footer Area -->"

if start_marker in html and end_marker in html:
    before = html.split(start_marker)[0]
    after = html.split(end_marker)[1]
    final_html = before + gallery_section + "\n    " + end_marker + after
    
    with open('gallery.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Created gallery.html")
else:
    print("Could not find markers!")
