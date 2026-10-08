from html import escape as e

def paragraphs(*items):
    return '</p><p>'.join(items)

def notes(title,items):
    return f'<div class="detail-block"><h3>{title}</h3><div class="detail-grid">'+''.join(f'<article><h4>{a}</h4><p>{b}</p></article>' for a,b in items)+'</div></div>'

def table(title,heads,rows):
    return f'<div class="detail-block"><h3>{title}</h3><div class="table-scroll" tabindex="0" role="region" aria-label="{e(title)}"><table><thead><tr>'+''.join(f'<th scope="col">{v}</th>' for v in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<{ "th scope=\"row\"" if i==0 else "td"}>{v}</{ "th" if i==0 else "td"}>' for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div></div>'

def sequence(title,items):
    return f'<div class="detail-block"><h3>{title}</h3><ol class="scenario-steps">'+''.join(f'<li><figure><img src="assets/{im}.webp" alt="{e(title+": "+name)}" loading="lazy" decoding="async"></figure><div><h4>{name}</h4><p>{text}</p></div></li>' for im,name,text in items)+'</ol></div>'

def S(id,title,intro,images=[],body=''):
    return (id,title,intro,images,[],[],body)

def enrich(projects):
    projects[0]['sections']=[
      S('research','The information gap in wildfire response.',paragraphs(
        'XFLARE is a graduation project developed with CES Advanced Composites & Defense Technologies Inc. as external advisor. It explores a connected drone controller and tactical smartwatch for forest firefighters, linking aerial observation to decisions made on the ground.',
        'The literature study focused on the consequences of missing or delayed information. Teams need to understand where people are, how the terrain changes, where the fire is moving and which routes remain usable. The project frames real-time situational awareness as the common requirement behind these problems.',
        'The research also examines the early “initial attack” period, described in the study as the first 30–60 minutes. This informed a design objective: reduce the time between arrival, aerial observation and a coordinated response.'),
        [('visual-03-00','Vehicle and terrain conditions considered in the wildfire research','photo'),('visual-03-02','Heat, smoke and heavy protective equipment define the operating context','photo')],
        notes('Four consequences of missing information',[
          ('Wrong strategy','Without knowing the location of campers or residents, a crew may concentrate on the fire while people remain at risk elsewhere.'),
          ('Resource mismatch','Missing information about fuel, vegetation and terrain can lead to unsuitable resources being dispatched—for example, a standard truck where aerial or earthmoving support is needed.'),
          ('Firefighter exposure','Wind shifts, spot fires and power lines can turn an apparently usable route into a trap. The system needs to support orientation as conditions change.'),
          ('Command blindness','Without a shared view of fire progression and road access, commanders struggle to coordinate units and establish escape routes.')])+
        notes('Risk themes that shaped the brief',[
          ('Physical strain','The literature review discusses overexertion, stress and cardiac events in relation to heavy equipment and extreme heat.'),
          ('Travel and response','Traffic and response crashes appear alongside on-scene hazards in the research, widening the context beyond firefighting itself.'),
          ('Loss of orientation','Smoke can remove visual references. This became a central reason to explore direct, glanceable guidance rather than relying only on verbal directions.')])+
        '<div class="detail-block"><h3>Wildfire context in the literature study</h3><p class="detail-lead">The research compares fire counts and burned area in Türkiye over 2015–2025, highlighting the difference between the number of incidents and their impact. The chart below is the comparison compiled for the project.</p><figure class="inline-diagram"><img src="assets/visual-03-01.webp" alt="Project research chart comparing forest-fire counts and burned area in Türkiye from 2015 to 2025" loading="lazy"></figure></div>'
      ),
      S('insights','From field research to design requirements.',paragraphs(
        'Interviews included a test pilot in the 401st Test Squadron, a UAV technician, an AKUT volunteer and a firefighter. Field photographs record the vehicles, protective clothing and attachment points examined during the research.',
        'Eight connected problems emerged. Each was translated into a specific requirement for the proposed system, rather than treated as a separate product feature.'),
        [('visual-04-00','Fire station visit and operational vehicles','photo'),('visual-04-01','Inspecting protective equipment and attachment details','photo'),('visual-04-06','Exploring how equipment is carried on protective clothing','photo')],
        table('Research finding → design response',['Finding','Implication for XFLARE'],[
          ('Orientation loss','Smoke can make visual references unusable. Provide intuitive directional guidance directly to field personnel; the research references the Eskişehir incident in this context.'),
          ('Information gap','A pilot’s verbal relay is slow and open to misinterpretation. Stream situational information to the hardware carried by ground crews.'),
          ('Communication dependency','GSM and messaging services can fail with damaged infrastructure. Explore an autonomous mesh network for closed-circuit coordination.'),
          ('Operational fragmentation','Separate agencies lack a common operational picture. Synchronise units around one shared situational-awareness map.'),
          ('Drones used in isolation','Treat the drone as an integrated, vehicle-mounted part of the response system, rather than an accessory that needs separate setup.'),
          ('Passive thermal monitoring','Thermal imagery should support the ground crew’s navigation, rather than remain confined to the pilot’s screen.'),
          ('Cognitive overload','Reduce menu complexity under environmental stress. Prioritise essential, glanceable information and direct controls.'),
          ('Deployment latency','Reduce assembly and calibration at the scene. “Zero-second deployment” is the project’s readiness objective, with the drone prepared before arrival.')])
      ),
      S('development','Initial Model',paragraphs(
        'During the pre-jury phase, I explored a convertible drone controller and smartwatch concept. I ultimately discarded this feature after realising it imposed design limitations.',
        'The transition scenario below shows the same early concept changing from a smartwatch into a drone controller. It records the six-stage transformation in order, before the project moved to separate devices.'),[],
        '<div class="detail-block"><h3>Transition Scenario</h3><ol class="initial-transition" aria-label="Original six-stage smartwatch-to-controller transition">'+''.join(f'<li><img src="assets/initial-transition-{i}.webp" alt="Step {i}: {label}" loading="lazy"></li>' for i,label in enumerate(['Smartwatch configuration','Strap and rotary control removal','Core device without attachments','Controller grip modules','Antenna installation','Drone controller configuration'],1))+'</ol></div>'+
        '<div class="detail-block"><h3>Initial Mock Up</h3><p class="detail-lead">The physical mock-up explores the same convertible concept in handheld and wrist-worn use.</p><div class="initial-mockups">'+''.join(f'<figure><img src="assets/{name}" alt="{label}" loading="lazy"><figcaption>{label}</figcaption></figure>' for name,label in [('initial-mockup-upright.svg','Initial physical mock-up'),('visual-05-06.webp','Wrist-worn configuration'),('visual-05-07.webp','Handheld configuration')])+'</div></div>'
      ),
      S('scenario','A connected response, from arrival to evacuation.',
        'The scenario follows commander Arda and a ground crew. It demonstrates the intended relationship between drone intelligence, command decisions and wrist-worn guidance; it is a proposed use sequence for the design.',[],
        sequence('Fireground use sequence',[
          ('fireground-scene-1','Arrive and launch','The firefighting vehicle reaches the scene. Its roof hatch opens and the reconnaissance drone launches to establish an aerial view.'),
          ('fireground-scene-2','Locate the fire','Arda watches the live feed on the handheld controller to identify the fire’s epicentre and understand the surrounding terrain.'),
          ('fireground-scene-3','Coordinate the response','Inside the vehicle, the commander reviews the tactical map and fire progression on the central dashboard display.'),
          ('fireground-scene-4','Mark a thermal finding','Arda identifies a tortoise in the thermal feed and marks its position. Ground personnel follow the alert on their watches to locate it.'),
          ('fireground-scene-5','Respond to a wind shift','A change in wind direction cuts off the crew’s route and leaves them disoriented within the fire.'),
          ('fireground-scene-6','Share an escape route','The commander plots an escape route on the controller. The crew receives that guidance on their watches and follows it out of danger.')])
      ),
      S('interface','One shared picture, two interfaces.',paragraphs(
        'The interface uses high-contrast dark surfaces and oversized interaction targets for smoke-filled environments and gloved hands. Information is organised around map, visual and thermal modes.',
        'The controller supports an overview of the operation; the watch brings immediate information to personnel in the field. Shared visual conventions connect both devices while the amount of information changes with the role.'),
        [('visual-07-01','Controller map: topographic context, personnel and waypoints','dark'),('visual-07-02','Controller visual feed: live optical view of the terrain','dark'),('visual-07-03','Controller thermal feed: infrared view of heat sources','dark')],
        table('Controller information hierarchy',['Control or feed','Purpose'],[
          ('Map view','Real-time topographic mapping and GPS locations of field personnel and assets for tactical coordination.'),
          ('Visual feed','Live optical video for terrain assessment, smoke monitoring and direct situational awareness.'),
          ('Thermal feed','Infrared imagery to identify active hot spots through dense smoke.'),
          ('Drone selection','Switch between drones within the shared operational system.'),
          ('Flight and environment data','Wind speed and direction, drone speed, compass and altitude remain available alongside the selected view.')])+
        sequence('Tactical smartwatch screens',[
          ('visual-07-05','Map and waypoints','Track the fire perimeter, squad positions and waypoints using a compact topographic view.'),
          ('visual-07-09','Visual feed','Receive live drone video directly on the wrist for awareness of smoke and terrain.'),
          ('visual-07-08','Thermal feed','View infrared information without depending solely on the drone operator’s screen.'),
          ('visual-07-10','Command alerts and SOS','Read incoming command messages and use a prominent tactical SOS control when assistance is needed.')])
      ),
      S('hardware','Physical controls for demanding conditions.',
        'The product language is rugged and deliberately tactile. The design combines screen interaction with dedicated buttons and mechanical details so that important functions are not buried in menus.',
        [('visual-09-07','Controller enclosure, antenna arrangement and tactical handles','dark'),('visual-09-04','Watch housing and retention bungees','dark'),('visual-09-09','Oversized textured rotary control','dark'),('visual-09-06','Protected connection and enclosure detail','dark')],
        notes('Drone controller details',[
          ('Handling and grip','Tactical handles allow the operator to free one hand. Rubber grip areas and a carabiner attachment point support carrying and retention.'),
          ('Dedicated commands','A power button, return-home button and autopilot mode provide physical access to recurring drone operations.'),
          ('Environmental provisions','The concept includes cooling vents and a protected waterproof charging-port design.')])+
        notes('Tactical smartwatch details',[
          ('Gloved operation','An oversized textured knob supports control while wearing gloves, alongside a separate power button.'),
          ('Emergency access','A physical SOS button provides an immediate control independent of the on-screen navigation.'),
          ('Retention and identification','Bungees secure the wearable, and an emergency ID tag is integrated into the design.')])
      ),
      S('technical','Construction and system architecture.',paragraphs(
        'Exploded views separate the enclosure, display, electronics, controls and retention components. The drawings explore assembly and material choices as part of the design proposal.',
        'The dimensioned watch study includes a 70 × 90 mm face envelope, 24 mm body depth and a Ø14 mm side control. Orthographic and sectional drawings show how both devices relate to the hand and wrist.'),
        [('exploded-watch','Tactical smartwatch exploded assembly'),('exploded-controller','Drone controller exploded assembly'),('technical-watch','Watch dimensions and sections; units in millimetres'),('technical-controller','Controller orthographic and sectional drawings')],
        table('Proposed component and material specification',['Assembly','Tactical smartwatch','Drone controller'],[
          ('Display protection','Sapphire crystal protective glass; AMOLED display','Sapphire crystal protective glass; AMOLED display'),
          ('Main housing','Titanium upper and back cases','Titanium upper and back cases'),
          ('Physical controls','ABS power button; aluminium rotary knob','ABS power, home and joystick components'),
          ('Charging and seals','Rubber charging-port cover; ABS charge unit; fluoroelastomer sealing O-ring','Ballistic nylon charging-port cover; electronic charge unit; fluoroelastomer sealing O-ring'),
          ('Electronics','Main PCB and lithium-polymer battery','Main PCB, secondary sub-PCB and lithium-polymer battery'),
          ('Retention and structure','Ballistic nylon straps, stainless-steel buckle and bungees','Steel carabiner hole and aluminium top handle'),
          ('Cooling and radio','Compact wearable enclosure','Aluminium-chassis cooling fan, stainless-steel mesh and titanium foldable RF antennas')])+
        '<div class="detail-block"><h3>Three operational layers</h3><p class="detail-lead">The aerial layer gathers information; the control layer coordinates the response; the ground layer receives guidance through the tactical watches. The diagram also positions a central control centre and aerial response vehicles in the broader system.</p><figure class="inline-diagram"><img src="assets/system-diagram.webp" alt="XFLARE system diagram connecting drones, ground crews, vehicle controllers and a central control centre" loading="lazy"></figure></div>'
      ),
      S('prototype','The physical model.',
        'The final controller and smartwatch models bring the separate-device direction into physical form. Together with the interface prototypes, they communicate the scale, control placement, protective language and relationship between the two products.',
        [('visual-10-01','Final XFLARE controller and tactical smartwatch physical models','photo')])
    ]

    projects[1]['sections']=[
      S('research','Understanding the electric bus as a system.',paragraphs(
        'HARMA E-BRT reinterprets Phrygian heritage through a retro-futuristic lens, translating Anatolian monumentality into an electric mobility identity for Ankara. The team project combines vehicle styling with passenger needs, route context and interior organisation.',
        'Benchmarking began with four-vehicle sketch studies across orthographic and perspective views. Form, character lines, colour, proportion and distinctive features were compared before a new vehicle language was developed.'),
        [('visual-13-00','Comparative vehicle analysis and sketch studies')],
        table('Literature research: key vehicle components',['Component','Design consideration'],[
          ('Front face','A recognisable arrangement of character lines and functional elements establishes brand identity and makes the bus easy to identify.'),
          ('Headlights and daytime running lights','A clear lighting signature improves visual readability in traffic—especially relevant for quiet electric vehicles.'),
          ('Door layout','Door position and opening width affect passenger flow, waiting time and the proportions of the side elevation.'),
          ('Side profile','Continuous character lines guide the eye along the vehicle and prevent a fragmented silhouette.'),
          ('Roof equipment','HVAC, battery packs and ventilation modules can be grouped within fairings or a continuous housing.'),
          ('Materials','The study considers composite panels and lightweight aluminium in relation to mass, impact resistance and structural strength.')])+
        notes('Visual identity across the benchmark set',[
          ('Recognisable silhouette','The analysed references include Mercedes eCitaro, MAN Lion’s City E, Isuzu Citiport, Volvo 7900, Solaris, Seoul city buses and Yutong U18.'),
          ('A coherent system','City colours, symbols and typography reinforce identity. A consistent visual language connects the exterior to the wider transport service.')])
      ),
      S('fieldwork','What 16 passengers and drivers revealed.',paragraphs(
        'Interviews with students, parents, older people, travellers and drivers identified friction points in urban transport. Observations also covered stop buttons, screens, first-aid provision, handholds and seating arrangements.',
        'The findings were translated into spatial, ergonomic and information requirements, shaping both the vehicle interior and the scenarios used to develop it.'),
        [('visual-15-00','Field observations: feedback controls, information screens, safety equipment, handholds and seats')],
        table('User needs and design opportunities',['User group','Observed difficulty','Design direction'],[
          ('METU students','Heavy backpacks, physical strain and unstable standing conditions; uncertainty about route information.','Bag-friendly spaces, standing support and reliable real-time information.'),
          ('Older passengers and parents','High steps, abrupt braking and quickly closing doors create anxiety.','Low-floor boarding, accessible support and smoother seating transitions.'),
          ('Passengers with luggage or trolleys','Narrow aisles and missing storage turn circulation into an obstacle course.','Dedicated luggage zones and clearer paths through the vehicle.'),
          ('Drivers','Crowding creates blind spots and makes doors harder to monitor; cabin comfort also matters.','Camera-assisted visibility and improved climate control.')])+
        notes('Three priorities',[
          ('Spatial logic','Separate backpack and luggage storage from the main circulation path.'),
          ('Ergonomics','Consider universal handrail heights and transitions that are manageable for children and older passengers.'),
          ('Communication','Use clear wayfinding and trustworthy digital information to reduce navigation stress.')])
      ),
      S('route','Why Gölbaşı–Çayyolu?',paragraphs(
        'The route study compared central and peripheral connections, including Kızılay–Ayrancı–Atakule, Tunalı–Ulus, ODTÜ–Kızılay, Kızılay–Çayyolu–Yaşamkent and connections towards Gölbaşı. Existing metro overlap, passenger variety and the opportunity for a distinct BRT service informed the choice.',
        'The selected Gölbaşı–Söğütözü–Koru alignment creates a direct connection that bypasses Kızılay and reduces reliance on multiple transfers. The proposal considers dedicated BRT lanes along the congested Eskişehir Yolu corridor.',
        'Residential, educational, commercial and medical destinations bring together students, workers, hospital visitors, shoppers and families. This variety makes accessibility and flexible interior space central to the vehicle brief.'),
        [('route-map','Selected Gölbaşı–Çayyolu corridor and route alignment')],
        table('Route context and passenger profiles',['Area','Implications for the vehicle'],[
          ('Gölbaşı','Residential origin with commuters, students and families; a strong morning flow towards Söğütözü, ODTÜ and Bilkent.'),
          ('Söğütözü','Transport and commercial hub serving AŞTİ travellers, offices and shopping destinations; substantial transfer activity.'),
          ('ODTÜ / METU','High-volume student travel, boarding waves around class changes and backpack-heavy passengers who need standing and circulation space.'),
          ('Bilkent and City Hospital','Shift-working hospital staff, visitors with accessibility needs and university students.'),
          ('Koru / Çayyolu','Residential destination and metro interchange with long-distance commuters and evening return flows.')])
      ),
      S('development','Phrygian references, contemporary form.',paragraphs(
        'The moodboards connect Phrygian artefacts, geometric forms and material references with a contemporary electric vehicle. The exploration includes ODTÜ Museum references and a palette of dark neutrals, greens, warm metallic tones and muted accents.',
        'The intention is to reinterpret heritage through proportion, surfaces and detail. The exterior and interior share the same geometric vocabulary, creating a consistent identity across different scales.'),
        [('visual-17-01','Phrygian artefacts, surface references and colour palette'),('visual-17-00','Broader inspiration and material moodboard')]),
      S('layout','Developing the passenger plan.',paragraphs(
        'Several plan arrangements explore seating, doors, standing capacity and accessible spaces. Sketches were tested through a physical interior model and digital layouts, then refined around the passenger needs identified in the research.',
        'The final plan distinguishes seating, accessibility, leaning, storage and door zones. A broad standing area accommodates dense passenger flows, while multi-use storage and LED surface lighting help organise the interior.'),
        [('visual-18-00','Alternative seating, door and accessibility arrangements'),('visual-18-03','Physical spatial model used during layout development'),('visual-18-01','Transition from the digital interior layout to functional zoning'),('visual-18-02','Final plan with seating, accessibility, leaning, storage and door zones')],
        notes('Decisions in the final plan',[
          ('Wide standing area','Maintain room for high passenger density on a busy corridor and reduce conflicts around the main path.'),
          ('Multi-use storage','Give backpacks and luggage defined places without treating every trip as a seated journey.'),
          ('Visible zoning','Use LED surface lights and the organisation of support elements to make the layout understandable.')])
      ),
      S('scenarios','Two journeys that test the interior.',
        'The passenger scenarios examine independence, physical effort and circulation. They connect the layout to everyday actions: identifying an entrance, boarding, placing belongings, using support and preparing to leave.',[],
        sequence('Parents with a stroller',[
          ('stroller-1','Find an accessible entry','Stop information and stroller symbols make the appropriate entry point visible before boarding. A level transition reduces lifting and physical effort.'),
          ('stroller-2','Reach the dedicated space','A clear interior path leads to the stroller area rather than forcing the parent to negotiate a crowded aisle.'),
          ('stroller-3','Use the adjacent seat','The folding seat provides a place for the parent next to the stroller while allowing the space to remain flexible.'),
          ('stroller-4','Place the bag nearby','An adjacent surface keeps belongings within reach and out of the circulation path.'),
          ('stroller-5','Travel with support','The parent can remain beside the stroller in an organised space with accessible handholds.'),
          ('stroller-6','Signal before leaving','A nearby stroller-related request control supports preparation for an accessible exit and reduces the need to ask others for help.')])+
        sequence('A student travelling with luggage',[
          ('luggage-1','Wait with reliable information','The journey begins at the stop with luggage and a clear view of the approaching service.'),
          ('luggage-2','Board without lifting into a high step','The accessible entrance allows the passenger to roll luggage into the vehicle.'),
          ('luggage-3','Place the luggage','A dedicated area keeps the bag stable and removes it from the main aisle.'),
          ('luggage-4','Stand with support','A leaning and support area lets the passenger remain near the luggage while preserving space for others during busy periods.')])
      ),
      S('details','A consistent identity inside and out.',paragraphs(
        'Exterior geometry combines Phrygian motifs with a contemporary electric vehicle aesthetic. The front and side views show how the lighting, glazing and body surfaces establish a continuous vehicle identity.',
        'Inside, ambient LED zoning and structural centre poles organise the passenger space. Seats and support details carry geometric Phrygian references into the parts of the vehicle passengers encounter directly.'),
        [('harma-profile-centered.svg','Exterior profile and lighting identity','profile-detail'),('visual-19-02','Street perspective and articulated body','photo'),('visual-20-00','Seat geometry and passenger environment','photo'),('visual-20-01','Structural poles and ambient lighting','photo'),('visual-20-02','Seating, glazing and accessible support','photo'),('visual-20-03','Central aisle and the continuity of the interior','photo')])
    ]

    projects[2]['sections']=[
      S('research','Healthcare access when infrastructure is disrupted.',paragraphs(
        'Mobile Infirmary is a portable medical unit designed to bring essential services to disaster-affected and rural areas. Distance, limited transport and damaged hospitals form the starting point of the project.',
        'The research considers situations in which hospitals and field tents are crowded, unreachable or damaged. Its emergency-response framing highlights the first 48 hours after a disaster as an important period for reaching people quickly.',
        'The population snapshot used in the project compares Türkiye’s 93.4% urban / 6.6% rural distribution with a global 57.5% urban / 42.5% rural distribution. These figures provide the study’s context for geographic access; they are not presented as measured rates of healthcare deprivation.'),
        [('visual-24-00','Mobile Infirmary concept positioned in a disaster-affected environment','photo')],
        notes('The design brief',[
          ('Reach remote areas','Carry a basic care environment towards communities facing long distances and limited transport.'),
          ('Reduce reliance on buildings','Provide a deployable space when local healthcare infrastructure is damaged or inaccessible.'),
          ('Organise different levels of care','Use distinct treatment zones and planned equipment storage within a compact mobile system.')])
      ),
      S('development','From vehicle volume to a deployable space.',paragraphs(
        'Initial digital models study the relationship between the vehicle chassis, enclosed volume and extending treatment areas. Front, side and rear views examine how the unit changes between transport and use.',
        'Early renders explore opening side panels, a rear entrance and colour-coded care areas in context. This stage establishes the main spatial idea before the final details and physical model are developed.'),
        [('visual-26-00','Initial rear volume and treatment-space study'),('visual-26-01','Early vehicle proportions and front perspective'),('visual-27-00','Initial render with an open treatment side','photo'),('visual-27-02','Early exploration of entrance and deployed side volume','photo')]),
      S('mockups','Testing the expansion physically.',paragraphs(
        'Cardboard and timber mock-ups make the opening sequence tangible. The model studies how a compact enclosure becomes a wider platform and how the side structure supports a treatment space.',
        'Open and closed configurations were reviewed alongside the digital work. The physical studies expose the relationships between the shell, folding elements, floor area and the space needed around the vehicle.'),
        [('visual-28-00','Early mock-up in a compact configuration','photo'),('visual-28-01','Examining the supporting structure and open platform','photo'),('visual-28-02','Expanded side space and working surface','photo'),('visual-28-05','Physical mock-up presented during the design review','photo')]),
      S('deployment','How the unit is set up.',
        'The storyboard describes a complete transition from travel to treatment. Curtains, poles and stretchers are carried as part of the vehicle so that the surrounding care spaces can be assembled on arrival.',[],
        sequence('Deployment and care sequence',[
          ('visual-29-02','Reach the site','The vehicle travels through difficult roads to bring primary healthcare to a rural disaster area.'),
          ('visual-29-03','Open the sides','A control inside the vehicle opens the flaps. An additional section slides forward to extend the usable space.'),
          ('visual-29-08','Assemble the enclosures','Curtains and poles stored in the rear compartment slide along a rail to form an enclosed treatment area.'),
          ('visual-29-04','Complete the enclosure','The remaining curtains are fixed to the vehicle and one another, and floor insulation is provided.'),
          ('visual-29-07','Position the stretchers','Stored stretchers are placed within the enclosed treatment area as the workspace is prepared.'),
          ('visual-29-06','Direct patients by need','The proposed workflow guides patients to green or red areas according to the severity of their condition.'),
          ('visual-29-01','Use the green zone','The design allocates examination, dressing and triage activities to the green treatment area.'),
          ('visual-29-00','Use the red zone','The red area is allocated to emergency interventions such as CPR, oxygen therapy and intubation in the proposed care programme.')])
      ),
      S('equipment','Equipment follows the care zones.',paragraphs(
        'The interior organisation links each care area to an equipment set. Shared supplies remain within the main unit, while the rear storage holds deployment and field equipment.',
        'This allocation is part of the project’s spatial programme: it shows what the design aims to accommodate and how supplies relate to different activities.'),
        [('visual-31-01','Rear view connecting the central unit to green and red treatment spaces','dark'),('visual-31-05','Internal storage and privacy curtain')],
        table('Treatment equipment and storage',['Zone','Allocated equipment'],[
          ('Green zone','Stethoscope; blood-pressure monitor; thermometer; height and weight measuring device; glucometer and test strips; portable ultrasound; otoscope / ophthalmoscope; dermatoscope; blood-collection kit and sample tubes.'),
          ('Red zone','Oxygen cylinder and mask system; emergency intervention kit; defibrillator; portable ECG; pulse oximeter; glucometer; blood-pressure monitor; pupillometer; patient record board and form storage.'),
          ('Main interior','Medication shelving; IV fluids, gloves, bandages and antiseptic supplies; portable printer and form binders; first-aid kits; disaster-specific supply boxes; sink and faucet.'),
          ('Rear storage','Curtains; first-aid kit; rope; toolbox and crowbar; stretcher; fire extinguisher; heavy-duty rope, with shovels and pickaxes shown in the equipment illustration.')])
      ),
      S('details','The interior and exterior, resolved together.',paragraphs(
        'The technical views document the vehicle’s internal organisation and the relationship between its side extensions and enclosed core. Storage, work surfaces and patient space are considered as parts of the same layout.',
        'Interior details include examination surfaces, a sink, cabinets, folding elements and a privacy curtain. Outside, red and green deployed zones make the intended functional separation visible, while the compact configuration retains the medical unit’s identity.'),
        [('visual-30-01','Side sectional view of the interior organisation'),('infirmary-technical-upright.svg','Technical interior view of the treatment and storage arrangement'),('visual-32-06','Examination area and internal circulation'),('visual-32-03','Sink and adjacent cabinet detail'),('visual-33-01','Expanded exterior configuration','dark'),('visual-33-02','Roof and compact exterior configuration','dark')]),
      S('prototype','Building the final model.',paragraphs(
        'The final physical model brings together the vehicle shell, storage compartments, side extensions and transparent treatment enclosures. It shows the design in both transport and deployed states.',
        'Multiple views document the interior access, side platforms and relationship between the two care areas. The model communicates the spatial proposal developed through the earlier mock-ups and digital studies.'),
        [('visual-34-00','Internal cabinets and access in the final model','photo'),('visual-34-01','Deployed side treatment enclosure','photo'),('visual-34-02','Vehicle front and expanded treatment space','photo'),('visual-34-04','Rear and side organisation','photo'),('visual-34-05','Compact enclosure and vehicle proportions','photo'),('visual-34-07','Final physical model presented for review','photo')])
    ]

    projects[3]['sections']=[
      S('overview','Different brands, different spatial needs.',
        'These projects were developed during my internship at ProDesign. The collection includes a café exterior, an initial and refined Puma pop-up proposal, and a Rioba coffee-festival stand. Each translates a different brief into a physical environment through form, display, lighting and visualisation.',
        [('visual-36-01','Alsancak Café exterior'),('visual-36-03','Puma modular retail concept'),('visual-36-00','Rioba coffee-festival stand'),('visual-36-02','Additional branded counter concept from the internship collection','dark')]),
      S('alsancak','Alsancak Café: a welcoming exterior.',paragraphs(
        'The brief was to create a warm, cosy exterior that encourages people to relax and enjoy their time. The design combines outdoor seating with a consistent canopy and lighting treatment across the café frontage.',
        'The renders show tables and stools along the façade, a covered edge and wall lighting that establishes the atmosphere. Overall and close-up views explore how the street-facing space reads from a distance and feels at seating level.'),
        [('visual-37-00','Overall café frontage, canopy and seating layout','photo'),('visual-37-02','View along the covered outdoor seating area','photo'),('visual-37-03','Wall lighting, material treatment and seating detail','photo')],
        notes('Spatial emphasis',[
          ('A continuous frontage','Repeated canopy supports and wall elements connect the seating area into one recognisable exterior.'),
          ('An inviting atmosphere','Warm light and the material palette support the relaxed, welcoming character described in the brief.')])
      ),
      S('puma','Puma: a compact pop-up proposal.',paragraphs(
        'The initial proposal was developed for shopping-mall placement. It combines Puma’s bold athletic identity with modular, easily installed elements intended to create a strong presence within a limited retail footprint.',
        'An open frame defines the stand without fully enclosing it. Clothing rails, shoe display and brand graphics occupy different faces, allowing the concept to be understood from more than one approach.'),
        [('visual-38-00','Initial Puma pop-up: overall structure and display faces'),('visual-38-02','Apparel display and rear approach'),('visual-38-03','Brand graphics and integrated display detail')],
        notes('Initial concept priorities',[
          ('Modularity','Develop a compact, easily installed spatial structure appropriate to a temporary retail setting.'),
          ('Visual impact','Use a bold frame, graphic surfaces and visible product to express the brand in a shared mall environment.'),
          ('Multiple display faces','Distribute apparel and footwear across the stand rather than relying on one front-facing elevation.')])
      ),
      S('refinement','Puma: refinement through brand feedback.',paragraphs(
        'The final version was refined in response to the brand’s feedback, with visibility, functionality and fit with the retail strategy as the stated priorities.',
        'The developed proposal has a more open, walk-in arrangement. A branded overhead frame, perimeter product display, central presentation unit and green floor define the retail area. The surrounding perspective illustrates how the stand reads within a larger interior.'),
        [('visual-39-00','Final Puma proposal in an interior setting','photo'),('visual-39-04','Overhead view of the final retail arrangement','dark'),('visual-39-02','Perimeter apparel and footwear display','photo'),('visual-39-03','Central display and brand communication','photo')],
        table('Development visible across the proposals',['Initial proposal','Refined proposal'],[
          ('A compact display structure organised around several exterior faces.','A walk-in retail area with an open perimeter and clearer internal circulation.'),
          ('Product and graphics concentrated within a small modular frame.','Product displays distributed around the perimeter with an additional central presentation element.'),
          ('Strong visual impact through contrasting graphics and structural edges.','A continuous overhead identity and defined floor area establish a larger, cohesive brand space.')])
      ),
      S('rioba','Rioba: a stand for the coffee festival.',paragraphs(
        'The Rioba stand was developed for a coffee festival, with the aim of expressing a premium identity while remaining inviting and functional in a competitive event environment.',
        'A roof-like frame establishes a visible silhouette above the service counter. Faceted shelving on the visitor-facing side, a clear working surface and the coffee equipment organise the stand at counter level. Alternate perspectives document the service side and the overall structural composition.'),
        [('visual-40-00','Rioba stand: overall form and service counter'),('visual-40-02','Alternate view of the roof frame and display shelving'),('visual-40-03','Working side and counter configuration')],
        notes('Design emphasis',[
          ('An identifiable silhouette','The elevated roof frame helps distinguish the stand in a crowded festival setting.'),
          ('A welcoming counter','The open visitor-facing edge makes the service area easy to approach.'),
          ('A coherent premium character','Material contrast, restrained colour and geometric display details carry the intended brand expression.')])
      )
    ]
