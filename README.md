# Materials IA
Useful references for Cambridge Materials Science IA course

## General Materials Science references:

The first point of reference for any course is the handouts and the lectures themselves. However, some students might find a different explanation more intuitive or might want to gain a deeper understanding of a particular topic. As a result, here I will try to compile some useful resources:
Many interactive learning packages have been created over the years at the Materials department present in [DoITPoMS](https://www.doitpoms.ac.uk/).
A general textbook that covers most of the topics in first-year materials can be found in *Callister, William D., and David G. Rethwisch. Materials science and engineering: an introduction. Vol. 9. New York: Wiley, 2018*.

In addition to this, a set of slides for each supervision can be found [here](https://universityofcambridgecloud-my.sharepoint.com/:f:/g/personal/grl31_cam_ac_uk/Enocz1Dbq7lCmznDKUwd5kgBeV1m5ZYsrrdTeimtmF3jPg?e=mF8zwB). Each supervision will have corresponding lecture summaries, topics that students often find tricky, some additional interesting content beyond the scope of the course, and a related exam question.

## Course A: Atomic structures of materials:

This is an introductory course into Crystallography, which is the study of how atoms are arranged into an ordered structure.
To help visualise some of these complex structures, the department has a license to CrystalMaker, which you can download onto your computer (highly recommended).
A useful database for theoretical and experimental data on materials' properties can be found in the [Materials Project](https://materialsproject.org/), for which is free to make an account.
To get familiar with the different symmetries, all the 230 different space groups can be found [here](http://img.chem.ucl.ac.uk/sgp/mainmenu.htm).
I noticed that one of my previous lecturers has also decided to make a [GitHub page](https://github.com/aronwalsh/Crystallography) for his course that he is teaching this year on Crystallography. I don't know exactly what he will cover and how frequently he will update the page throughout the term, but it might be useful, especially since he shows how to set up CrystalMaker.

## Course B: Materials for Devices:

This course covers a variety of technologically relevant properties that certain types of materials have, in particular electrical and magnetic properties that are covered in more depth in *Moulson, Anthony J., and John M. Herbert. Electroceramics: materials, properties, applications. John Wiley & Sons, 2003* book.

## Course C: Diffraction:

This course covers how to characterise crystalline materials by their difraction pattern when interacting with X-rays or electrons. 
To reconstruct the crystalline structure from the resulting diffraction pattern, we need to be able to convert between real and reciprical space, which unfortunately cannot be mathematically understood without covering Fourier transforms, which is usually done in the second year. As such, I have created a Jupyter notebook that you can run on your browser that goes through some of these concepts, which you can find [here](https://colab.research.google.com/github/Gio-A-Oakes/Materials_IA/blob/main/Jupyter_notebooks/Reciprical%20space.ipynb#scrollTo=lp80hNY4pkmA).

## Course D: Microstructure:

The mechanical properties of a material are not only dependent on the crystalline structure, but also its microstructure as different phases can be presemt.
The microstructure that forms depends both on the thermodynamics and the kinetics between the different phases that are possible to form.
A neat way to look into the thermodynamics is by using Monte Carlo simulations, which can be found [here](https://colab.research.google.com/github/Gio-A-Oakes/Materials_IA/blob/main/Jupyter_notebooks/Gmix.ipynb#scrollTo=tKUsb58oBp18).
A useful textbook that covers this course is [*Porter, David A., and Kenneth E. Easterling. Phase transformations in metals and alloys (revised reprint). CRC Press, 2009.*](https://ezp.lib.cam.ac.uk/login?url=https://search.ebscohost.com/login.aspx?direct=true&db=nlebk&AN=1763501&site=ehost-live&scope=site).
Alternative lectures and lecture notes on this topic can be found [here](https://dyedavid.com/mse104/).

## Course E: Mechanical Behaviour of Materials:

This course looks at how different structures covered in course A and D affect the mechanical properties of materials.
A good reference on dislocations, can be found in [*Hull, Derek, and David J. Bacon. Introduction to dislocations. Butterworth-Heinemann, 2001.*
](https://idiscover.lib.cam.ac.uk/permalink/f/t9gok8/44CAM_ALMA51621314410003606)

A jupyter notebook on the mechanical and thermol properties that can be obtained from an inter-atomic potential can be found [here](https://colab.research.google.com/github/Gio-A-Oakes/Materials_IA/blob/main/Jupyter_notebooks/Lennard-Jones%20potential.ipynb#scrollTo=WNU1Ir-0kcG4).

## Course F: Biomaterials:

The body is a very harsh and dynamic environment, as a result there are only a handful of materials that are bio-compatable. In this course materials-selection charts will be covered to select the most appropritate materials used for different bio-applications.

## Course G: Materials under Extreme Conditions:

This course looks at how extreme conditions such as high pressure, temperature and radiation affect material properties and means of mitigating material degredation. For example we will cover how [single crystal Ni superalloys are used in turbine blades in jet engines above their melting temperature](https://www.youtube.com/watch?v=aFRdp1Js9Kc). 
