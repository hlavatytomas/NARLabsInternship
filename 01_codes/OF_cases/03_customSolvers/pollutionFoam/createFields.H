Info<< "Reading field T\n" << endl;

volScalarField yPol
(
    IOobject
    (
        "yPol",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);


Info<< "Reading field U\n" << endl;

volVectorField U
(
    IOobject
    (
        "U",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);


Info<< "Reading physicalProperties\n" << endl;

IOdictionary physicalProperties
(
    IOobject
    (
        "physicalProperties",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE
    )
);


Info<< "Reading molar diffusivity DT\n" << endl;

dimensionedScalar DT
(
    physicalProperties.lookup("DT")
);

dimensionedScalar Sc
(
    physicalProperties.lookup("Sc")
);

volScalarField nut
(
    IOobject
    (
        "nut",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

volScalarField Dturb
(
    IOobject
    (
        "Dturb",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    // mesh
    nut/Sc

);

#include "createPhi.H"

#include "createFvModels.H"
#include "createFvConstraints.H"
